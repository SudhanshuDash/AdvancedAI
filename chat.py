from chatterbot import ChatBot

# This is the terminal client for the assignment
chatbot = ChatBot(
    'MyAssignmentBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///bot_database.sqlite3'
)

print("🤖 ChatterBot Terminal Client (Assignment)")
print("Type your message and press Enter.")
print("Type 'quit' to stop chatting.\n")

while True:
    user_input = input("user: ").strip()
    
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("bot: Goodbye! Have a nice day! 👋")
        break
    
    if user_input == "":
        continue
        
    response = chatbot.get_response(user_input)
    print(f"bot: {response}\n")