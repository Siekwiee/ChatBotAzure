from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot("HatBot")

# Create a new instance of a ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train("chatterbot.corpus.english")

# Main loop for chatting
print("HatBot: Hello! I'm HatBot. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("HatBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("HatBot:", response)