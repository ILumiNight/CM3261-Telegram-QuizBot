import telebot # must install module to laptop
from telebot import types
import random
import time

bot_token = #insert token

bot = telebot.TeleBot(bot_token)

overall = dict()
checking = False

def stuff():
    return dict(
        topic = "", # chosen topic
        count = 0, # track round number
        total = 0, # total number of rounds
        current_question = None, # qn from question bank
        current_answer = None, # ans from quesion bank
        points = {}, # keeps track of points scored
        correct_name = "", # notes person who provided correct answer
        chance = 0,
        sending = False
    )

question_bank = {
"Element Cycles" : {
    "Nutrient cycles are also known as _ _ _ _ _ _ _ _ _ _ _ _ _ _ cycles.": "Biogeochemical",
    "The amount of time nutrients spend in a pool or reservoir is known as the _ _ _ _ _ _ _ _ _   _ _ _ _.": "Residence Time",
    "The rate at which materials move between reservoirs is known as _ _ _ _": "Flux",
    "A _ _ _ _ _ _ is a reservoir that releases more materials than it accepts.": "Source",
    "A _ _ _ _ is a reservoir that accepts more materials than it releases.": "Sink",
    "In 2001, what percentage of the Eastern Oyster population fell? _ _": "99",
    "Name this reason for the destruction of the Chesapeake Bay oyster reefs. P _ _ _   W _ _ _ _   Q _ _ _ _ _ _": "Poor Water Quality",
    "Name this reason for the destruction of the Chesapeake Bay oyster reefs. R _ _ _   D _ _ _ _ _ _ _ _ _ _": "Reef Destruction",
    "Name this reason for the destruction of the Chesapeake Bay oyster reefs. V _ _ _ _ _ _ _   D _ _ _ _ _ _ _": "Virulent Diseases",
    "Name this reason for the destruction of the Chesapeake Bay oyster reefs. O _ _ _ __ _ _ _ _ _ _ _ _": "Overharvesting",
    "What was constructed to support the Chesapeake Bay oyster population? _ _ _ _ _ _ _ _ _ _   _ _ _ _ _": "Artificial Reefs",
    "Human activity has caused the increased flux of _ _ _ _ _ _ _ _ from the atmosphere to the reservoirs on Earth's surface.": "Nitrogen",
    "Human activity has caused the increased flux of _ _ _ _ _ _ from the reservoirs on Earth's surface to the atmosphere.": "Carbon",
    "Carbon escapes from the Earth reservoir to the atmosphere in the form of _ _ _ _ _ _   _ _ _ _ _ _ _.": "Carbon Dioxide",
    "Water moves from oceans, lakes, ponds, rivers, and moist soil into the atmosphere via _ _ _ _ _ _ _ _ _ _ _.": "Evaporation",
    "Name this factor which speeds up evaporation. W _ _ _   T _ _ _ _ _ _ _ _ _ _ _": "Warm Temperatures",
    "Name this factor which speeds up evaporation. S _ _ _ _ _   W _ _ _ _": "Strong Winds",
    "Name this factor which speeds up evaporation. G _ _ _ _ _ _   D _ _ _ _ _   O _   E _ _ _ _ _ _ _": "Greater Degree Of Exposure",
    "The release of water vapour by plants through their leaves is known as _ _ _ _ _ _ _ _ _ _ _ _ _.": "Transpiration",
    "Name this natural process of distillation. E _ _ _ _ _ _ _ _ _ _": "Evaporation",
    "Name this natural process of distillation. T _ _ _ _ _ _ _ _ _ _ _ _": "Transpiration",
    "Water enters the Earth's surface from the atmosphere in the form of _ _ _ _ _ _ _ _ _ _ _ _ _.": "Precipitation",
    "What is the factor that gives rise to Earth's variety of biomes? _ _ _ _ _ _ _ _ _ _ _ _ _": "Precipitation",
    "Water found beneath layers of soil is known as _ _ _ _ _ _ _ _ _ _ _.": "Groundwater",
    "A sponge-like region of rock and soil that is an underground reservoir of water is known as _ _ _ _ _ _ _.": "Aquifer",
    "The upper limit of groundwater held in an aquifer is known as the _ _ _ _ _   _ _ _ _ _.": "Water Table",
    "What human activity causes the slowing down of movement of water from the land to the sea? D _ _ _ _ _ _   R _ _ _ _ _": "Damming Rivers",
    "What human activity causes an increase in evaporation of water? H _ _ _ _ _ _   W _ _ _ _   I _   R _ _ _ _ _ _ _ _ _": "Holding Water In Reservoirs",
    "What human activity causes an increase in surface runoff? R _ _ _ _ _ _ _   N _ _ _ _ _ _   V _ _ _ _ _ _ _ _ _": "Removing Natural Vegetation",
    "The withdrawl of surface water and groundwater causes the lowering of _ _ _ _ _   _ _ _ _ _ _.": "Water Tables",
    "The natural distillation process is sabotaged via E _ _ _ _ _ _ _   O _   P _ _ _ _ _ _ _ _ _   into the atmosphere.": "Emission Of Pollutants",
    "The routes that carbon atoms take through the environment is described by the _ _ _ _ _ _   _ _ _ _ _.": "Carbon Cycle",
    "Name the biological process by which carbon is removed from the atmosphere and converted to organic molecules. _ _ _ _ _ _ _ _ _ _ _ _ _ _": "Photosynthesis",
    "Carbon dioxide and water are produced when carbohydrates are broken down in _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _ _ _.": "Cellular Respiration",
    "Organisms use carbon for S _ _ _ _ _ _ _ _ _  G _ _ _ _ _.": "Structural Growth",
    "Sediments experiencing high pressure over long periods of time result in the conversion of _ _ _ _   _ _ _ _ _ _ _   into fossil fuels.": "Soft Tissues",
    "Carbon trapped in sediments and fossil fuel deposits can be naturally released into the oceans or atmosphere via G _ _ _ _ _ _ _   P _ _ _ _ _ _ _ _.": "Geologic Processes",
    "Carbon trapped in sediments and fossil fuel deposits can re-enter the atmosphere via the burning of F _ _ _ _ _   F _ _ _ _.": "Fossil Fuels",
    "Since the mid-18th century, how many billion tons of carbon dioxide has been added into the atmosphere through the combustion of fossil fuels? _ _ _": "276",
    "Absorbtion of carbon dioxide by ocean water causes an increase in its A _ _ _ _ _ _.": "Acidity",
    "What percentage of nitrogen makes up our atmosphere? _ _": "78",
    "The process of converting nitrogen gas into ammonium ions is known as _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _.": "Nitrogen Fixation",
    "Nitrogen fixation can be accomplished by the intense energy of _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _.": "Lightning Strikes",
    "Nitrogen fixation can be accomplished when air in the top layer of soil contacts with _ _ _ _ _ _ _ _ - _ _ _ _ _ _   _ _ _ _ _ _ _ _.": "Nitrogen-fixing Bacteria",
    "Nitrogen-fixing bacteria live in a M _ _ _ _ _ _ _ _ _ _ relationship with many types of plants.": "Mutualistic",
    "The process of converting ammonium ions into nitrite ions, then into nitrate ions, and finally to nitrogen gas, is known as _ _ _ _ _ _ _ _ _ _ _ _ _ _ _.": "Denitrification",
    "D _ _ _ _ _ _ _ _ _ _ _   B _ _ _ _ _ _ _ converts nitrates in soil or water to nitrogen gas.": "Denitrifying Bacteria",
    "The rate of nitrogen fixation had doubled with the development of the _ _ _ _ _ - _ _ _ _ _   _ _ _ _ _ _ _.": "Haber-Bosch process",
    "The amount of nitrogen returning to the atmosphere is reduced due to the destruction of W _ _ _ _ _ _ _.": "Wetlands",
    "Name this impact of the farming practice of speed runoff. N _ _ _ _ _ _ _   P _ _ _ _ _ _ _ _": "Nutrient Pollution",
    "Name this impact of the farming practice of speed runoff. E _ _ _ _ _ _ _ _ _ _ _ _ _": "Eutrophication",
    "Name this impact of the farming practice of speed runoff. H _ _ _ _ _ _": "Hypoxia",
    "The burning of fossil fuels releases N _ _ _ _ _   O _ _ _ _   into the atmosphere.": "Nitric Oxide",
    "Name this essential soil nutrient that can be stripped due to the over-application of nitrogen-based fertilizers. C _ _ _ _ _ _": "Calcium",
    "Name this essential soil nutrient that can be stripped due to the over-application of nitrogen-based fertilizers. P _ _ _ _ _ _ _ _": "Potassium",
    "How is the phosphorus contained in rocks released? _ _ _ _ _ _ _ _ _ _": "Weathering",
    "_ _ _ _ _ _ _ _ _ _ _   is a frequent limiting factor for plant growth.": "Phosphorus",
    "In a 2008 study, how much phosphorus, in kilograms, did the Chesapeake Bay receive per year? _ . _ _": "4.52",
},

"Lithosphere" : {
    "What is defined as the practice of raising crops and livestock for human use and consumption? _ _ _ _ _ _ _ _ _ _ _": "Agriculture",
    "What is defined as land used to raise plants for human use? _ _ _ _ _ _ _ _": "Cropland",
    "What is defined as land used for grazing livestock? _ _ _ _ _ _ _ _ _": "Rangeland",
    "What percentage of the Earth's surface does rangeland cover? _ _": "26",
    "What percentage of the Earth's surface does cropland cover? _ _": "12",
    "What kind of soil is vital for sustainable agriculture? _ _ _ _ _ _ _": "Healthy",
    "Sustainable agriculture requires reliable sources of C _ _ _ _   W _ _ _ _.": "Clean Water",
    "Sustainable agriculture requires minimized usage of fossil fuel-based F _ _ _ _ _ _ _ _ _ _.": "Fertilizers",
    "Sustainable agriculture requires healthy populations of P _ _ _ _ _ _ _ _ _ _   I _ _ _ _ _ _.": "Pollinating Insects",
    "Sustainable agriculture requires sustenance of G _ _ _ _ _ _   D _ _ _ _ _ _ _ _.": "Genetic Diversity",
    "G _ _ _ _ _ _   M _ _ _ _ _ _ _ _ _ _ _   is a method for sustainable agriculture.": "Genetic Modification",
    "Name this main nutrient soil provides to enable plant growth. N _ _ _ _ _ _ _": "Nitrogen",
    "Name this main nutrient soil provides to enable plant growth. P _ _ _ _ _ _ _ _ _": "Phosphorus",
    "O _ _ _ _ _ _   M _ _ _ _ _   provides nutrients and helps with soil structure and water retention.": "Organic Matter",
    "Name this type of agriculture that involves manual farming by humans and animal muscle power. _ _ _ _ _ _ _ _ _ _ _": "Traditional",
    "Name this type of agriculture that involves producing only enough food for farming families. _ _ _ _ _ _ _ _ _ _ _": "Subsistence",
    "Name this type of agriculture that involves large-scale mechanization. _ _ _ _ _ _ _ _ _ _": "Industrial",
    "By volume, what is the percentage of mineral in soil? _ _": "50",
    "By volume, what is the percentage of organic matter in soil? _": "5",
    "Name this type of weathering for the process of soil formation. P _ _ _ _ _ _ _": "Physical",
    "Name this type of weathering for the process of soil formation. C _ _ _ _ _ _ _": "Chemical",
    "Name this type of weathering for the process of soil formation. B _ _ _ _ _ _ _ _ _": "Biological",
    "What is defined as organic substance resulting from the breakdown of planet material? _ _ _ _ _": "Humus",
    "What is each layer of soil known as? _ _ _ _ _ _ _": "Horizon",
    "What is the cross section of soil as a whole known as? _ _ _ _   _ _ _ _ _ _ _": "Soil Profile",
    "The 'A Horizon' category corresponds to _ _ _ _ _ _ _.": "Topsoil",
    "The 'B Horizon' category corresponds to _ _ _ _ _ _ _.": "Subsoil",
    "The 'C Horizon' category corresponds to _ _ _ _ _ _ _ _ _   _ _ _ _ _   _ _ _ _ _ _ _ _.": "Weathered Plant Material",
    "Minerals move down the soil profile as a result of _ _ _ _ _ _ _ _.": "Leaching",
    "What is this physical property of soil that indicates composition and fertility. _ _ _ _ _ _": "Colour",
    "What is this physical property of soil that is determined by the size of particles. _ _ _ _ _ _ _": "Texture",
    "What is this physical property of soil that measures the 'clumpiness' of soil. _ _ _ _ _ _ _ _ _": "Structure",
    "What is this physical property of soil that affects the availability of nutrients. _ _": "pH",
    "What is the lower limit for the pH range of soil? _": "4",
    "What is the upper limit for the pH range of soil? _ _": "10",
    "What is the chemical process by which plants gain nutrients from the soil? _ _ _ _ _ _   _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _": "Cation Exchange Capacity",
    "What series describes the relative strength of various cations' adsorption to colloids? _ _ _ _ _ _ _ _ _ _": "Hofmeister",
    "What is defined as the ability to capture different nutrients and ions? _ _ _ _ _ _ _ _": "Sorption",
    "What occurs during chemical reactions when a nutrient or chemical in the soil solution transforms into a solid? _ _ _ _   _ _ _ _ _ _ _ _ _ _ _ _ _": "Soil Precipitation",
    "The main source of electrons in soils is _ _ _ _ _ _   _ _ _ _ _.": "Carbon atoms",
    "The main source of protons in soils is _ _ _ _ _": "Water",
    "Name this cause of soil erosion. D _ _ _ _ _ _ _ _ _ _ _ _": "Deforestation",
    "Name this cause of soil erosion. C _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _ _ _": "Cropland Agriculture",
    "Name this cause of soil erosion. O _ _ _ _ _ _ _ _ _ _": "Overgrazing",
    "What is the percentage of reduced potential rates of food production on cropland due to soil degradation? _ _": "13",
    "What is the percentage of reduced potential rates of food production on rangeland due to soil degradation? _": "4",
    "Name this factor that affects mobility of heavy metals. p _": "pH",
    "Name this factor that affects mobility of heavy metals. R _ _ _ _   R _ _ _ _ _ _ _ _": "Redox Reactions",
    "Name this factor that affects mobility of heavy metals. Concentration of   D _ _ _ _ _ _ _ _   O _ _ _ _ _ _   M _ _ _ _ _": "Dissolved Organic Matter",
},

"Waste Management" : {
    "What type of waste is a non-liquid waste that comes from homes, institutions and small businesses? _ _ _ _ _ _ _ _ _   _ _ _ _ _   _ _ _ _ _": "Municipal Solid Waste",
    "What type of waste includes waste from production of consumer goods, mining, agriculture and petroleum extraction and refining? _ _ _ _ _ _ _ _ _ _   _ _ _ _ _   _ _ _ _ _": "Industrial Solid Waste",
    "What type of waste is a solid or liquid waste that is toxic, chemically reactive, flammable or corrosive? _ _ _ _ _ _ _ _ _   _ _ _ _ _": "Hazardous Waste",
    "What approach to waste management involves minimizing waste at the source? _ _ _ _ _ _   _ _ _ _ _ _ _ _ _": "Source Reduction",
    "What approach to waste management involves recycling and composting? _ _ _ _ _ _ _ _": "Recovery",
    "What approach to waste management involves burying waste in landfills and burning waste in incinerators? _ _ _ _ _ _ _ _": "Disposal",
    "What is layered along with waste to speed decomposition, reduce odour and lesson infestation by pests? _ _ _ _": "Soil",
    "What encourages biodegradation by bacteria when introduced to landfills? _ _ _ _ _ _ _ _ _": "Rainwater",
    "Incineration reduces the weight of municipal waste by up to _ _ %": "75",
    "Incineration reduces the volume of municipal waste by up to _ _ %": "90",
    "What gas is produced in an incinerator, which can be converted to energy? _ _ _ _ _ _ _": "Methane",
    "What base is used to remove hazardous components and neutralize acidic gases in incenerators? _ _ _ _ _ _ _   _ _ _ _ _": "Calcium Oxide",
    "How many million tonnes of material did recycling divert away from incinerators and landfills in the U.S. in 2010? _ _": "65",
    "How many steps are involved in recycling? _": "3",
    "_ _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _   seeks to make industry more sustainable.": "Industrial Ecology",
    "By definition, hazardous waste should be I _ _ _ _ _ _ _ _.": "Ignitable",
    "By definition, hazardous waste should be C _ _ _ _ _ _ _ _.": "Corrosive",
    "By definition, hazardous waste should be R _ _ _ _ _ _ _.": "Reactive",
    "By definition, hazardous waste should be T _ _ _ _.": "Toxic",
    "Which disposal method of hazardous waste involves several impervious liners and leachate removal systems? _ _ _ _ _ _ _ _ _": "Landfills",
    "Which disposal method is meant for liquid hazardous waste? _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _ _ _ _": "Surface Impoundments",
    "Which disposal method is meant for long term disposal of hazardous waste? _ _ _ _   _ _ _ _   _ _ _ _ _ _ _ _ _": "Deep Well Injection",
},

"Food Chain" : {
    "The human population is expected to reach _ billion by the middle of the century.": "9",
    "Name this factor allowing for sustainable food supply. H _ _ _ _ _ _   _ _ _ _": "Healthy Soil",
    "Name this factor allowing for sustainable food supply. W _ _ _ _": "Water",
    "Name this factor allowing for sustainable food supply. B _ _ _ _ _ _ _ _ _ _ _": "Biodiversity",
    "What term describes people who receive fewer calories than the minimum dietary energy requirement? _ _ _ _ _ _ _ _ _ _ _ _ _ _": "Undernutrition",
    "What term describes people who lead sedentary lives with little exercise amidst an abundance of food? _ _ _ _ _ _ _ _ _ _ _ _ _": "Overnutrition",
    "What term describes the shortage of nutrients the body needs? _ _ _ _ _ _ _ _ _ _ _ _": "Malnutrition",
    "What improves the efficiency of planting and harvesting, at the expense of pest outbreaks and reduced biodiversity? _ _ _ _ _ _ _ _ _ _ _ _": "Monocultures",
    "What resulted due to the desire for greater food quantity and quality? _ _ _ _ _   _ _ _ _ _ _ _ _ _ _": "Green Revolution",
    "What type of agriculture does not deplete soils faster than they form? _ _ _ _ _ _ _ _ _ _ _": "Sustainable",
    "Eating lower on the food chain results in a smaller   _ _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _": "Ecological Footprint",
    "What is known for having factory farms and concentrated animal feeding operations? _ _ _ _ _ _ _": "Feedlot",
    "Feedlot allows for   E _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _ _.": "Economic Efficiency",
    "Feedlot allows for   G _ _ _ _ _ _   _ _ _ _   _ _ _ _ _ _ _ _ _ _.": "Greater Food Production",
    "_ _ _ _ _ _ _ _ _   _ _ _ _ _ causes eutrophication due to its richness in nitrogen and phosphorus": "Livestock Waste",
    "_ _ _ _ _ _ _ _ _ _ _   is the cultivation of aquatic organisms for food in controlled environments.": "Aquaculture",
    "What is an approach to preserving crop diversity? S _ _ _   V _ _ _ _": "Seed Vault",
    "What type of agriculture describes farming and ranching that uses lesser amoutns of pesticides, fertilizers, growth hormones, antibiotics, water and fossil fuel energy? _ _ _ - _ _ _ _ _": "Low-input",
    "What type of agriculture relies purely on biological approaches? _ _ _ _ _ _ _": "Organic",
    "What is an approach to organic agriculture? _ _ _ _ _ _ _ _ _ _": "Composting",
    "What GM food was engineered to fight vitamin A deficiency? _ _ _ _ _ _   _ _ _ _": "Golden Rice",
    "What GM food was engineered for it to have fast growth and large sizes? _ _ _ _ _ _": "Salmon",
    "What GM food was engineered with genes from BT bacterium to kill insects? _ _   _ _ _ _": "Bt Corn",
    "What crop has the highest percentage of GM food? _ _ _ _ _ _ _": "Soybean",
    "Amino acids, aspartame, and sodium ascorbate are chemicals commonly present in   _ _   _ _ _ _": "GM Food",
},

"Environmental Toxicology" : {
    "What major environmental health hazard arises from processes that occur naturally in the environment? _ _ _ _ _ _ _ _": "Physical",
    "What major environmental health hazard arises from synthetic chemicals? _ _ _ _ _ _ _ _": "Chemical",
    "What major environmental health hazard arises from ecological interaction among organisms? _ _ _ _ _ _ _ _ _ _": "Biological",
    "What major environmental health hazard arises from residence, socioeconomic status, occupatation and behavioural choices?. _ _ _ _ _ _ _": "Culture",
    "_ _ _ _ _ _ _ _ _ _   disease accounts for 1 of every 4 deaths each year.": "Infectious",
    "Name this factor that influences the spread of infectious diseases through increased mobility and dense human population. _ _ _ _ _ _": "Social",
    "Name this factor that influences the spread of infectious diseases through human-induced global warming. _ _ _ _ _ _ _ _ _ _ _ _ _": "Environmental",
    "Name this viral disease that spread due to increased mobility and dense human population. S _ _ _": "SARS",
    "What is defined as the intentional genetic manipulations of a pathogenic organisam to increase its virulence and transmission between humans? _ _ _ _ _ _ _ _ _ _ _ _": "Bioterrorism",
    "What is defined as the study of chemical hazards and the examination of effects of poisonous substances on humans and other organisms? _ _ _ _ _ _ _ _ _ _": "Toxicology",
    "Name this type of study that assesses toxic levels in the environment, using the information to determine potential past, present and future impacts. _ _ _ _ _ _ _ _ _ _ _ _ _": "Retrospective",
    "Name this type of study that uses specific tests to assess the likely impacts of chemicals or mixtures. _ _ _ _ _ _ _ _ _ _ _": "Prospective",
    "What is defined as any chemical, of natural or synthetic origin, capable of causing harmful effect on a living organism? _ _ _ _ _ _ _ _": "Toxicant",
    "Name this source of environmental toxicants that are discrete discharges of chemicals. _ _ _ _ _": "Point",
    "Name this source of environmental toxicants that are diffused over large areas. _ _ _ - _ _ _ _ _": "Non-point",
    "Name this type of exposure that is a risk posed by a hazard for short periods of time at high concentrations. _ _ _ _ _": "Acute",
    "Name this type of exposure that is a risk posed by a hazard for long periods of time at low concentrations. _ _ _ _ _ _ _": "Chronic",
    "What is defined as the accumulation of toxicants in an animal's body? _ _ _ _ _ _ _ _ _ _ _ _ _ _ _": "Bioaccumulation",
    "What is the result of individuals consuming many others from the trophic level beneath it, leading to increased concentrations in a body? _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _": "biomagnification",
    "What is defined as the amount of substance the test animal receives? _ _ _ _": "Dose",
    "What is defined as the type or magnitude of negative effects exhibited by the animals due to an introduced dosage? _ _ _ _ _ _ _ _": "Response",
    "Plotting this is a method to studying the effects of hazard. _ _ _ _ - _ _ _ _ _ _ _ _   _ _ _ _ _": "Dose-response Curve",
    "Below the   _ _ _ _ _ _ _ _ _   on a dose-response curve, doses have no measureable effect.": "threshold",
    "Name this type of interaction between toxicants, whereby a combination of 2 or more chemicals is the sum of the expected individual responses. _ _ _ _ _ _ _ _ _ _": "Additivity",
    "Name this type of interaction between toxicants, whereby exposure to 1 chemical results in a reduced effect of another. _ _ _ _ _ _ _ _ _ _": "Antagonism",
    "Name this type of interaction between toxicants, whereby exposure to 1 chemical results in a greater effect of another. _ _ _ _ _ _ _ _ _ _ _ _": "Potentiation",
    "Name this type of interaction between toxicants, whereby exposure to 1 chemical causes a dramatic increase in effect of another. _ _ _ _ _ _ _ _ _": "Synergism",
    "Name this analysis to risk assessment. H _ _ _ _ _   _ _ _ _ _ _ _ _ _ _ _ _ _ _": "Hazard Identification",
    "Name this analysis to risk assessment. D _ _ _": "Dose",
    "Name this analysis to risk assessment. E _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _ _": "Exposure Assessment",
    "Name this analysis to risk assessment. R _ _ _   _ _ _ _ _ _ _ _ _ _": "Risk evaluation",
    "What policy approach involves bringing products to the market quickly after limited testing? _ _ _ _ _ _ _ _   _ _ _ _ _   _ _ _ _ _ _   _ _ _ _ _ _": "Innocent Until Proven Guilty",
    "What policy approach involves bringing products to the market cautiously after extensive testing? _ _ _ _ _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _": "Precautionary Principle",
    "What is one policy approach done in the US? _ _ _ _ _   _ _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _   _ _ _": "Toxic Substances Control Act",
    "What is one policy approach done in European countries? _ _ _ _ _   _ _ _ _ _ _ _": "REACH Program",
},

"Infectious Diseases" : {
    "Which country in Asia has the highest prevalence of extended-spectrum beta-lactamase (ESBL) producers (i.e. a type of resistance)? _ _ _ _ _": "India",
    "Which type of microorganisms may be treated with antibiotics? _ _ _ _ _ _ _ _": "Bacteria",
    "What threatens the environment and human health? _ _ _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _ _ _": "Antibiotic Resistance",
    "Name a type of mediicine that cannot be disposed of at home. _ _ _ _ - _ _ _ _ _ _   _ _ _ _ _ _ _ _": "Anti-cancer medicine",
    "Where are antibiotics found in the environment? _ _ _ _": "Soil",
    "Name a process by which antibiotic resistance may develop naturally. _ _ _ _ _ _ _ _": "Mutation",
    "Describe an effect of antibiotic resistance on human health. _ _ _ _   _ _ _ _ _ _": "More deaths",
    "Medicines used to treat this chronic disease may be disposed of at home. _ _ _ _ _ _ _ _": "Diabetes",
}
}

# command "help"
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Use /start to start a game!\n' + "Use /stop to stop a game!")

# command "stop"
@bot.message_handler(commands=['stop'])
def stop(message):
    global overall
    if message.chat.id in overall:
        bot.reply_to(message, "Session stopped!")
        del overall[message.chat.id]
    else:
        bot.reply_to(message, "There is no quiz in progress!")

# command "start"
@bot.message_handler(commands=['start'])
def category(message):
    if message.chat.id in overall: #prevents starting a new game when one is in progress
        bot.send_message(message.chat.id, "❌ Quiz is already in progress! ❌")
        return
    else:
        overall[message.chat.id] = stuff() #creates game for specific chat id
        markup = types.ReplyKeyboardMarkup(row_width = 2, one_time_keyboard = True, selective = True)
        for topic in list(question_bank.keys()):
            markup.add(types.KeyboardButton(topic))
        markup.add(types.KeyboardButton('All'))
        msg = bot.reply_to(message, "✨ Choose a topic! ✨", reply_markup=markup) #asks user to choose topic
        bot.register_next_step_handler(msg, rounds)

def rounds(message):
    global overall
    if message.text in list(question_bank.keys()) or message.text == "All":
        overall[message.chat.id]["topic"] = message.text #locks topic
        markup = types.ReplyKeyboardMarkup(row_width = 2, one_time_keyboard = True, selective = True)
        for length in ['5', '10', '15']:
            markup.add(types.KeyboardButton(length))
        msg = bot.reply_to(message, "⏳ How many rounds? ⏳", reply_markup=markup) #asks user to choose no. of rounds
        bot.register_next_step_handler(msg, conclusion)
    else:
        bot.send_message(message.chat.id, "Message not recognized. Session stopped!")
        del overall[message.chat.id]

def conclusion(message):
    global overall
    if message.text in ["5", "10", "15"]:
        overall[message.chat.id]["total"] = int(message.text) #locks rounds
        msg = bot.send_message(message.chat.id, "Let\'s play! You have selected" +
        '\nTopic: ' + str(overall[message.chat.id]["topic"]) + '\nRounds: ' + str(overall[message.chat.id]["total"]))
        markup = types.ReplyKeyboardMarkup(row_width = 2, one_time_keyboard = True, selective = True)
        for response in ["Yes", "No"]:
            markup.add(types.KeyboardButton(response))
        msg = bot.reply_to(message, "Are you ready to begin?", reply_markup=markup) #asks user to confirm start of quiz
        bot.register_next_step_handler(msg, start_quiz)
    else:
        bot.send_message(message.chat.id, "Message not recognized. Session stopped!")
        del overall[message.chat.id]

def start_quiz(message):
    global overall
    if message.text.lower() == 'yes':
        ask_question(message)
    elif message.text.lower() == "no":
        bot.send_message(message.chat.id, "Session stopped!")
        del overall[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Message not recognized. Session stopped!")
        del overall[message.chat.id]

def ask_question(message):
    """Asks a qn with a timeout"""
    global overall
    if overall[message.chat.id]["count"] >= overall[message.chat.id]["total"]:
        end_quiz(message)
        return
    # choose question bank
    if overall[message.chat.id]["topic"] in list(question_bank.keys()):
        bank = question_bank[overall[message.chat.id]["topic"]]
    else:
        bank = random.choice(list(question_bank.values()))

    overall[message.chat.id]["sending"] = False
    time.sleep(2)

	#set a question and save to global state
    if message.chat.id in overall:
        overall[message.chat.id]["count"] += 1
        overall[message.chat.id]["correct_name"] = ""
        overall[message.chat.id]["current_question"] = random.choice(list(bank)) #locks new question
        overall[message.chat.id]["current_answer"] = bank[overall[message.chat.id]["current_question"]] #locks answer to question
        overall[message.chat.id]["chance"] = 5

    #show users the round
        bot.send_message(message.chat.id, "📝 Question " + str(overall[message.chat.id]["count"])
        + "/" + str(overall[message.chat.id]["total"]) + " 📝")
        bot.send_message(message.chat.id, overall[message.chat.id]["current_question"]) #show users the question
        overall[message.chat.id]["sending"] = True

    return

def end_quiz(message): #points announcement
    overall[message.chat.id]["points"] = sorted(overall[message.chat.id]["points"].items(), key=lambda x: x[1], reverse=True)
    temp = "```\n"
    for key, value in overall[message.chat.id]["points"]:
        temp = temp + "{0:<20} {1}".format(key, str(value)) + "\n"
    temp += "```"

    bot.send_message(message.chat.id, "🏁 End of the round! 🏁")
    del overall[message.chat.id] #reset game variables
    bot.send_message(message.chat.id, "🔥 Here are the scores! 🔥")
    bot.send_message(message.chat.id, temp, parse_mode = "Markdown")

@bot.message_handler(func=lambda message: message.chat.id in overall and overall[message.chat.id]["sending"])
def check_answer(message):
    global overall
    global checking
    while checking:
        continue
    checking = True
    if message.chat.id in overall:
        if overall[message.chat.id]["current_answer"] != None:
            if message.text.lower() == overall[message.chat.id]["current_answer"].lower():
                name = message.from_user.username #note points
                overall[message.chat.id]["correct_name"] = name #note person
                bot.send_message(message.chat.id, "🎉 Nice! " + overall[message.chat.id]["correct_name"] +
                " got it! 🎉" + "\nThe answer was: " + overall[message.chat.id]["current_answer"])
                if name not in overall[message.chat.id]["points"]:
                    overall[message.chat.id]["points"][name] = 1
                else:
                    overall[message.chat.id]["points"][name] += 1
                ask_question(message)
            else:
                overall[message.chat.id]["chance"] -= 1
                if overall[message.chat.id]["chance"] == 0:
                    bot.send_message(message.chat.id, "No chances left! The correct answer was "
                    + overall[message.chat.id]["current_answer"])
                    ask_question(message)
                else:
                    bot.send_message(message.chat.id, "Wrong! You have " + str(overall[message.chat.id]["chance"])
                    + " chance(s) remaining!")
    checking = False
    return

while True:
    bot.polling()
