from dotenv import load_dotenv
import os
import speech_recognition as speech
import pygame
from gtts import gTTS
import time
from src.baseChat import ChatGPT

def play_audio(audio_file):
    pygame.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.unload()

def save_audio(response):
    language = 'fr'
    tts = gTTS(text=response, lang=language)
    audio_file = "audio/response.mp3"
    reponseDynamique = int(time.time())
    new_file_name = "audio/" + str(reponseDynamique) + ".mp3"
    tts.save(new_file_name)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(new_file_name)


    while pygame.mixer.music.get_busy():
        continue
    if os.path.exists(audio_file):
        os.remove(audio_file)
    return new_file_name


def get_audio_input(recognizer, microphone, language='fr'):
    with microphone as source:
        print("Parlez s'il vous plaît...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        print("Merci !")

    try:
        # using Google Speech Recognition
        text = recognizer.recognize_google(audio, language=language)
        print(f"Vous avez dit: {text}")
        return text
    except speech.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit.")
    except speech.RequestError as e:
        print(
            "Désolé, je ne peux pas accéder à Google Speech Recognition. Code d'erreur : {0}".format(e))


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("CHATGPT_API_KEY")
    chat_gpt = ChatGPT(api_key)

    recognizer = speech.Recognizer()
    microphone = speech.Microphone()

    print("Bienvenue ! Je suis votre assistant vocal. Pour quitter, dites simplement 'au revoir'.")

    is_awake = False  # variable pour savoir si l'assistant est réveillé ou non
    while True:
        if not is_awake:  # vérifier si l'assistant est réveillé
            user_message = get_audio_input(recognizer, microphone)
            if user_message and user_message.lower() == "hey pascal":  # si l'utilisateur dit "Hey Fanta"
                print("Oui ?")
                play_audio("audio/wake_up.mp3")
                is_awake = True
        else:  # sinon, traiter la demande de l'utilisateur avec OpenAI
            print("Traitement en cours...")
            user_message = get_audio_input(recognizer, microphone)
            if user_message:
                if user_message.lower() == "au revoir":  # si l'utilisateur dit "au revoir"
                    print("Au revoir !")
                    chat_gpt.add_message("user", user_message)
                    response = "Au revoir !"
                    chat_gpt.add_message("assistant", response)
                    audio_file = save_audio(response)
                    play_audio(audio_file)
                    break
                else:
                    chat_gpt.add_message("user", user_message)
                    response = chat_gpt.get_response(user_message)
                    chat_gpt.add_message("assistant", response)
                    audio_file = save_audio(response)
                    play_audio(audio_file)
                    print(response)
                    if 'ouvre' in response.lower():
                        app = response.split('ouvre')[-1].strip()
                        os.system(f'start "" "{app}"')