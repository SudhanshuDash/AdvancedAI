from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the bot
chatbot = ChatBot(
    'MyBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///bot_database.sqlite3'
)

# Train the bot with English conversations
trainer = ChatterBotCorpusTrainer(chatbot)
print("Training the bot... This takes 30-60 seconds the first time. Please wait...")
trainer.train("chatterbot.corpus.english")

print("✅ Training finished! You can now run the chat.")