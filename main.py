import json
import logging

from telegram.ext import Updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO,
)

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Make a bot
    updater = Updater(config['token'])
    
    # Load data into the bot to be accessed later on.
    updater.dispatcher.bot_data['quiz'] = config['quiz']
    
    # Load handlers into the bot (in order of priority)
    import quiz
    updater.dispatcher.add_handler(quiz.handler)

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
