# Very Simple Chatbot
import random

print("Welcome to ChatBot!")
print("Type 'help' for options, 'bye' to exit.\n")

running = True

while running:
    user_input = input("You: ").lower().strip()
    
    if user_input == "":
        continue
    
    # Exit
    if user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Bot: Goodbye!")
        running = False
        break
    
    # Greetings
    elif user_input in ["hello", "hi", "hey"]:
        print("Bot:", random.choice(["Hello!", "Hi there!", "Hey!"]))
    
    # How are you
    elif "how are you" in user_input:
        print("Bot:", random.choice(["I'm great!", "I'm fine, thanks!", "All good!"]))
    
    # Name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot:", random.choice(["I'm ChatBot!", "My name is ChatBot."]))
    
    # Help
    elif user_input == "help":
        print("Bot: I can respond to: hello, how are you, your name, joke, weather, bye")
    
    # Joke
    elif "joke" in user_input:
        print("Bot:", random.choice([
            "Why don't scientists trust atoms? They make up everything!",
            "What do you call a fake noodle? An impasta!"
        ]))
    
    # Weather
    elif "weather" in user_input:
        print("Bot: I can't check weather, but it's nice in here!")
    
    # Default
    else:
        print("Bot:", random.choice([
            "I don't understand.",
            "Try saying 'help'.",
            "Can you rephrase that?"
        ]))
    
    print()