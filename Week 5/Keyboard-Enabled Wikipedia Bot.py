# This Python script allows users to ask questions by typing them in through the keyboard. It utilizes the Wikipedia API to search for relevant information 
# based on the question and provides a textual response along with text-to-speech synthesis

import speech_recognition as sr
import wikipedia
import pyttsx3

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Get input from keyboard
question = input("Ask me a question: ")

# Search Wikipedia for relevant information
try:
    results = wikipedia.search(question)
    if len(results) > 0:
        page = wikipedia.page(results[0])
        answer = page.content
        print(answer)

        # Convert answer to speech and play it
        engine.say(answer)
        engine.runAndWait()
    else:
        print("Sorry, I could not find any information related to your question on Wikipedia.")

except wikipedia.exceptions.PageError:
    print("Sorry, I could not find any information related to your question on Wikipedia.")
except wikipedia.exceptions.DisambiguationError as e:
    page = wikipedia.page(e.options[0])
    answer = page.content
    print(answer)

    # Convert answer to speech and play it
    engine.say(answer)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError:
    print("Sorry, I could not access the Google Speech Recognition API.")

