import openai
import os
import pygame
from google.cloud import texttospeech
from translatepy import Translator

# Initialize OpenAI API
openai.api_key = "insert key here"

# Function to convert text to speech using Google Text-to-Speech API
def text_to_speech(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="fr-FR", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
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

# Function to translate text to French using Translatepy
def translate_to_french(text):
    translator = Translator()
    translated_text = translator.translate(text, destination_language="French")
    return translated_text.result

# Main function to get user input, generate responses using ChatGPT API, translate to French, and play text-to-speech audio
def main():
    user_input = input("Ask me a question: ")
    print("Getting chatbot response...")

    chatgpt_response = get_chatgpt_response(user_input)
    print(f"ChatGPT (English): {chatgpt_response}")

    print("Translating response to French...")
    french_response = translate_to_french(chatgpt_response)
    print(f"ChatGPT (French): {french_response}")

    print("Converting text to speech...")
    chatgpt_audio_file = text_to_speech(french_response)

    pygame.mixer.init()

    print("Playing ChatGPT response...")
    pygame.mixer.music.load(chatgpt_audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    main()
