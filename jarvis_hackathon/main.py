"""Entry point for Jarvis voice-enabled chatbot.
Features:
- Listen to voice commands (SpeechRecognition)
- Speak responses (pyttsx3)
- Open websites (webbrowser)
- Simple text-mode fallback and demo commands for hackathon use
"""

from jarvis import JarvisAssistant

def main():
    jarvis = JarvisAssistant(voice_name='Jarvis')
    print("Jarvis is ready. Say 'help' or type 'help' to see commands.")
    jarvis.run()  # starts interactive voice/text loop

if __name__ == '__main__':
    main()
