import speech_recognition as sr
import pyttsx3
import time

def safe_listen(recognizer: sr.Recognizer, timeout=5, phrase_time_limit=7):
    """Try to listen from the default microphone and return recognized text.
    Returns None if microphone not available or recognition fails.
    """
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print('Please speak...')
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print('Could not understand audio.')
            return None
        except sr.RequestError as e:
            print('Speech recognition service error:', e)
            return None
    except Exception as e:
        print('Microphone not available or error:', e)
        return None

def speak_text(engine, text: str):
    """Speak using pyttsx3 engine and also print to console."""
    try:
        print('Jarvis:', text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print('TTS error:', e)
