# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import wikipedia
import random

# Define some basic responses
greetings = ['hi', 'hello', 'hey']
goodbyes = ['bye', 'goodbye', 'see you later']
thanks = ['thank you', 'thanks', 'appreciate it']
options = ['tell me a joke', 'what is your name?', 'what time is it?', 'how is the weather?', 'tell me about a historical event']

# Set up speech recognition
r = sr.Recognizer()

# Set up text-to-speech engine
engine = pyttsx3.init()

# Define the chatbot function
def chatbot():
    # Greet the user
    print("Bot: Hi, I'm a chatbot. How can I help you?")

    # Start the conversation
    while True:
        # Listen for user input
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)

        try:
            # Recognize user input
            user_input = r.recognize_google(audio).lower()

            # Respond to user input
            if user_input in greetings:
                engine.say("Hi there!")
                engine.runAndWait()
            elif user_input in goodbyes:
                engine.say("Goodbye!")
                engine.runAndWait()
                break
            elif user_input in thanks:
                engine.say("You're welcome!")
                engine.runAndWait()
            elif user_input == options[0]:
                engine.say("Why did the chicken cross the road? To get to the other side!")
                engine.runAndWait()
            elif user_input == options[1]:
                engine.say("My name is Chatbot.")
                engine.runAndWait()
            elif user_input == options[2]:
                import datetime
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                engine.say("The current time is " + current_time + ".")
                engine.runAndWait()
            elif user_input == options[3]:
                engine.say("I'm sorry, I don't have access to the internet to check the weather.")
                engine.runAndWait()
            elif user_input == options[4]:
                # Get a random historical event from Wikipedia
                event = wikipedia.random(pages=1)
                summary = wikipedia.summary(event, sentences=2)
                engine.say(summary)
                engine.runAndWait()
            else:
                engine.say("Sorry, I didn't understand what you said.")
                engine.runAndWait()

        except sr.UnknownValueError:
            # Handle unrecognized speech input
            engine.say("Sorry, I didn't understand what you said.")
            engine.runAndWait()

        except sr.RequestError:
            # Handle speech recognition service errors
            engine.say("Sorry, I couldn't connect to the speech recognition service.")
            engine.runAndWait()

# Start the chatbot
chatbot()
