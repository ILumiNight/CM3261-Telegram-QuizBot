import random

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    Filters,
)

# Application states that affect which handlers are active
CHOOSE_A_TOPIC, HOW_MANY_QUESTIONS, RUNNING_QUIZ = range(3)

# Helper functions to manage the quiz
def send_question(data):
    """Takes in a dictionary with some data to update the bot data and run a question."""
    chat_id = data['chat_id']
    context = data['context']

    # Update question and answer
    choices = list(context.bot_data['quiz'][context.chat_data['topic']].keys())
    question = random.choice(choices)
    solution = context.bot_data['quiz'][context.chat_data['topic']][question]

    # Add helper blanks to question
    question += "\n"
    for char in solution:
        if char != " ":
            question += "_ "
        else:
            question += "   "

    context.chat_data['question'] = question
    context.chat_data['solution'] = solution
    context.chat_data['display_solution'] = solution

    # Send question
    context.bot.send_message(chat_id, question)

def run_quiz(context: CallbackContext):
    """Sends a question"""
    data = context.job.context
    chat_id = context.job.context['chat_id']
    data['context'].chat_data['number'] += 1

    # Send question number and question
    current = data['context'].chat_data['number']
    total = data['context'].chat_data['total']
    context.bot.send_message(chat_id, f'Question {current} / {total}')
    send_question(data)

    # Set time limit for each question
    context.job_queue.run_once(latency, 15, context=data, name=str(data['chat_id']))

    return RUNNING_QUIZ

def latency(context: CallbackContext):
    """Prevents the duplication of job scheduling due to latency issues"""
    data = context.job.context

    # Prevent answer trigger
    data['context'].chat_data['solution'] = ''

    # Set time delay to prevent job duplication
    context.job_queue.run_once(no_answer, 1, context=data, name=str(data['chat_id']))

    return RUNNING_QUIZ

def no_answer(context: CallbackContext):
    """Displays answer if question had not been answered"""
    data = context.job.context
    chat_id = context.job.context['chat_id']
    current = data['context'].chat_data['number']
    total = data['context'].chat_data['total']

    # Display answer
    soln = data['context'].chat_data['display_solution']
    context.bot.send_message(chat_id, f'Nobody answered. It was {soln}.')

    # Schedule run_quiz if there are more questions
    if current < total:
        context.job_queue.run_once(run_quiz, 3, context=data, name=str(data['chat_id']))# Delay time to next question, question not answered

    # Schedule end_quiz if there are no more questions
    else:
        context.job_queue.run_once(end_quiz, 3, context=data, name=str(data['chat_id']))# Delay time to end quiz, question not answered

    return RUNNING_QUIZ

def end_quiz(context: CallbackContext):
    """Sends a message to inform the user that there are no more questions"""
    data = context.job.context
    chat_id = context.job.context['chat_id']

    # Display scores
    context.bot.send_message(chat_id, f'No more questions!')
    temp = "Here are the scores!\n"
    temp += "```\n"
    for id, tag in data['context'].chat_data['user'].items():
        key = tag['name']
        value = tag['points']
        temp = temp + "{0:<20} {1}".format(key, str(value)) + "\n"
    temp += "```"
    context.bot.send_message(chat_id, temp, parse_mode = "Markdown")

    # Return to original state
    return ConversationHandler.END

# Update handlers (Application state can be changed by returning a new state)
def start(update: Update, context: CallbackContext):
    """Prompt the user to set a topic"""
    # Prompt for topic
    update.message.reply_text(f'Choose a topic!', reply_markup = ReplyKeyboardMarkup(keyboard = [[topic] for topic in context.bot_data['quiz']], resize_keyboard = True, one_time_keyboard = True))

    return CHOOSE_A_TOPIC

def not_a_topic(update: Update, context: CallbackContext):
    """Handle bad input from user"""
    text = update.message.text
    update.message.reply_text(f'{text} is not an available category, please use the keyboard provided!')

    return CHOOSE_A_TOPIC

def set_topic (update: Update, context: CallbackContext):
    """Fix the topic for the current quiz instance, then prompt the user to set question number"""

    # Fix topic
    context.chat_data['topic'] = update.message.text
    chat_id = update.message.chat_id

    # Prompt for number of questions
    rounds = ["5", "10", "15"]
    update.message.reply_text(f'How many questions?', reply_markup = ReplyKeyboardMarkup(keyboard = [rounds], resize_keyboard = True, one_time_keyboard = True))

    return HOW_MANY_QUESTIONS

def not_a_number(update: Update, context: CallbackContext):
    """Handle bad input from user"""
    text = update.message.text
    update.message.reply_text(f'{text} is not an available number of questions, please use the keyboard provided!')

    return HOW_MANY_QUESTIONS

def set_number(update: Update, context: CallbackContext):
    """Set the number of qns for the chat and schedules the quiz as a job that repeatedly re-schedules itself"""

    # Fix number of questions
    context.chat_data['number'] = 0
    context.chat_data['total'] = int(update.message.text)
    chat_id = update.message.chat_id

    # Create dictionary for future score input
    context.chat_data['user'] = dict()

    # Start the quiz
    data = {'chat_id': chat_id,'context': context}
    context.job_queue.run_once(run_quiz, 3, context=data, name=str(chat_id))# Delay time to 1st question

    return RUNNING_QUIZ

def check_answer(update: Update, context: CallbackContext):
    """Checks if user input matches the answer to the current question"""
    cleaned_text = update.message.text.strip().lower()
    cleaned_soln = context.chat_data['solution'].strip().lower()
    if cleaned_text == cleaned_soln:

        # Cancel current question
        chat_id = update.message.chat_id
        data = {'chat_id': chat_id,'context': context}
        chat_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
        for job in chat_jobs:
            job.schedule_removal()

        # Update chat with answer
        name = update.message.from_user.first_name
        soln = context.chat_data['solution']
        update.message.reply_text(f'Correct! {name} got the right answer! It was {soln}.')

        # Prevent answer trigger
        context.chat_data['solution'] = ''

        # Update scores
        user_id = update.message.from_user.id
        if user_id not in context.chat_data['user']:
            context.chat_data['user'][user_id] = dict()
        context.chat_data['user'][user_id]['name'] = name
        context.chat_data['user'][user_id]['points'] = context.chat_data['user'][user_id].get('points', 0) + 1

        # Schedule run_quiz if there are more questions
        if context.chat_data['number'] < context.chat_data['total']:
            context.job_queue.run_once(run_quiz, 3, context=data, name=str(chat_id))# Delay time to next question, question answered

        # Schedule end_quiz if there are no more questions
        else:
            context.job_queue.run_once(end_quiz, 3, context=data, name=str(chat_id))# Delay time to end quiz, question answered

def error(update: Update, context: CallbackContext):
    """Generic handler for any user input that doesn't match any handlers"""
    update.message.reply_text('Sorry! I don\'t understand you!')

def end(update: Update, context: CallbackContext):
    """Ends the conversation"""

    # Cancel current question
    chat_id = update.message.chat_id
    data = {'chat_id': chat_id,'context': context}
    chat_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    for job in chat_jobs:
        job.schedule_removal()

    # Informs user that quiz was stopped
    update.message.reply_text('Quiz stopped!')

    # Return to original state
    return ConversationHandler.END

# Allows choice for active handlers
handler = ConversationHandler(
    entry_points = [
        CommandHandler('start', start),
    ],
    states = {
        CHOOSE_A_TOPIC: [
            MessageHandler(Filters.regex(r"^(Element Cycles|Lithosphere|Waste Management|Food Chain|Environmental Toxicology})$"), set_topic),
            MessageHandler(Filters.text, not_a_topic),
        ],
        HOW_MANY_QUESTIONS: [
            MessageHandler(Filters.regex(r"^(5|10|15)$"), set_number),
            MessageHandler(Filters.text, not_a_number),
        ],
        RUNNING_QUIZ: [
            MessageHandler(Filters.text & (~Filters.command), check_answer),
        ]
    },
    fallbacks = [
        CommandHandler('start', start),
        CommandHandler('end', end),
        MessageHandler(Filters.text, error)
    ],
    per_user = False
)
