from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Old dataset removed. Training new dataset")
except:
	print('No dataset found. Creating new dataset.')

english_bot = ChatBot('Bot')
english_bot.set_trainer(ListTrainer)
for file in os.listdir('data'):
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        english_bot.train(convData)
        print("Training completed for "+file)
    

