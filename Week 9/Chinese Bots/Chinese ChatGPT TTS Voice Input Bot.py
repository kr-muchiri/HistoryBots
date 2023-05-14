import openai
import os
import pygame
from google.cloud import texttospeech
from translatepy import Translator
import speech_recognition as sr

# Initialize OpenAI API
openai.api_key = "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"

# Function to get voice input
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask me a question: ")
        audio = recognizer.listen(source)
    
    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        print("Unable to understand the audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

# Function to convert text to speech using Google Text-to-Speech API
def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="zh-CN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    with open("output.wav", "wb") as out:
        out.write(response.audio_content)

    return "output.wav"

# Function to get response from OpenAI's GPT-3 API
def get_chatgpt_response(input_text):
    chatgpt_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=1000,
        n=10,
        stop=None,
        temperature=0.7,
    )

    return chatgpt_response.choices[0].text.strip()

# Function to translate text to Chinese using Translatepy
def translate_to_chinese(text):
    translator = Translator()
    translated_text = translator.translate(text, destination_language="Chinese")
    return translated_text.result



# Main function to get user input, generate responses using ChatGPT API, translate to Chinese, and play text-to-speech audio
def main():
    user_input = get_voice_input()
    if user_input is None:
        exit()

    print("You asked:", user_input)

    print("Getting chatbot response...")
    chatgpt_response = get_chatgpt_response(user_input)
    print(f"ChatGPT (English): {chatgpt_response}")

    print("Translating response to Chinese...")
    chinese_response = translate_to_chinese(chatgpt_response)
    print(f"ChatGPT (Chinese): {chinese_response}")

    print("Converting text to speech...")
    chatgpt_audio_file = text_to_speech(chinese_response)

    pygame.mixer.init()

    print("Playing ChatGPT response...")
    pygame.mixer.music.load(chatgpt_audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
