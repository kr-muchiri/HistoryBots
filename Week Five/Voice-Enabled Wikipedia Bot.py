## This code allows the user to ask a question verbally, converts the speech into text using speech recognition, searches Wikipedia for relevant 
# information based on the question, and provides both a textual and spoken answer using text-to-speech synthesis.

import speech_recognition as sr
import wikipedia
import pyttsx3

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

def get_audio_input():
    with sr.Microphone() as source:
        print("Listening for your question...")
        audio = r.listen(source)

    try:
        print("Recognizing your question...")
        recognized_text = r.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        print("Unable to understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Get input from microphone
question = get_audio_input()
if question is None:
    exit()

print("You asked:", question)

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
