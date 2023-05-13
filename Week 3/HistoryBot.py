# Import necessary libraries
import wikipedia
import random

# Define some basic responses
greetings = ['hi', 'hello', 'hey']
goodbyes = ['bye', 'goodbye', 'see you later']
thanks = ['thank you', 'thanks', 'appreciate it']
options = ['tell me a joke', 'what is your name?', 'what time is it?', 'how is the weather?', 'tell me about a historical event']

# Define the chatbot function
def chatbot():
    # Greet the user
    print("Bot: Hi, I'm a chatbot. How can I help you?")

    # Start the conversation
    while True:
        # Receive user input
        user_input = input("User: ").lower()

        # Respond to user input
        if user_input in greetings:
            print("Bot: Hi there!")
        elif user_input in goodbyes:
            print("Bot: Goodbye!")
            break
        elif user_input in thanks:
            print("Bot: You're welcome!")
        elif user_input == options[0]:
            print("Bot: Why did the chicken cross the road? To get to the other side!")
        elif user_input == options[1]:
            print("Bot: My name is Chatbot.")
        elif user_input == options[2]:
            import datetime
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Bot: The current time is " + current_time + ".")
        elif user_input == options[3]:
            print("Bot: I'm sorry, I don't have access to the internet to check the weather.")
        elif user_input == options[4]:
            # Get a random historical event from Wikipedia
            event = wikipedia.random(pages=1)
            summary = wikipedia.summary(event, sentences=4)
            print("Bot: " + summary)
        else:
            print("Bot: Sorry, I didn't understand what you said.")

# Start the chatbot
chatbot()