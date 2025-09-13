import webbrowser
import speech_recognition as sr
import pyttsx3
import sys
import re
from utils import safe_listen, speak_text

class JarvisAssistant:
    def __init__(self, voice_name='Jarvis'):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        # optional: adjust voice properties
        try:
            voices = self.engine.getProperty('voices')
            if voices:
                self.engine.setProperty('voice', voices[0].id)
            self.engine.setProperty('rate', 150)
        except Exception:
            pass
        self.name = voice_name

    def handle_command(self, command: str) -> bool:
        """Process a single command string. Returns False if the assistant should exit."""
        cmd = command.lower().strip()
        if not cmd:
            speak_text(self.engine, "I didn't catch that. Please say a command or type 'help'.")
            return True

        # exit
        if cmd in ('exit', 'quit', 'bye', 'stop', 'shutdown'):
            speak_text(self.engine, 'Shutting down. Good luck with your hackathon!')
            return False

        if cmd in ('help', 'commands'):
            help_text = (
                "Available commands:\n"
                " - open youtube\n"
                " - open google\n"
                " - open github\n"
                " - search for <query>\n"
                " - open <website> (e.g. open stack overflow)\n"
                " - say <your message> (Jarvis will echo)\n"
                " - help\n"
                " - exit\n"
            )
            print(help_text)
            speak_text(self.engine, 'Shown available commands in the console.')
            return True

        # direct open examples
        if 'open youtube' in cmd:
            speak_text(self.engine, 'Opening YouTube')
            webbrowser.open('https://www.youtube.com')
            return True
        if 'open google' in cmd:
            speak_text(self.engine, 'Opening Google')
            webbrowser.open('https://www.google.com')
            return True
        if 'open github' in cmd or 'open git hub' in cmd:
            speak_text(self.engine, 'Opening GitHub')
            webbrowser.open('https://github.com')
            return True

        # open generic known short names -> map common names to URLs
        known_sites = {
            'stack overflow': 'https://stackoverflow.com',
            'stackoverflow': 'https://stackoverflow.com',
            'gmail': 'https://mail.google.com',
            'google drive': 'https://drive.google.com',
            'drive': 'https://drive.google.com',
            'gmail': 'https://mail.google.com',
            'linkedin': 'https://www.linkedin.com',
            'twitter': 'https://twitter.com',
            'reddit': 'https://www.reddit.com'
        }
        for name, url in known_sites.items():
            if f'open {name}' in cmd:
                speak_text(self.engine, f'Opening {name}')
                webbrowser.open(url)
                return True

        # search command
        m = re.match(r'search for (.+)', cmd)
        if m:
            query = m.group(1)
            speak_text(self.engine, f'Searching Google for {query}')
            webbrowser.open(f'https://www.google.com/search?q=' + query.replace(' ', '+'))
            return True

        # open arbitrary website like: open example.com or open example
        m2 = re.match(r'open (.+)', cmd)
        if m2:
            target = m2.group(1).strip()
            # if looks like domain
            if '.' in target:
                url = target if target.startswith('http') else 'https://' + target
            else:
                url = 'https://www.' + target.replace(' ', '') + '.com'
            speak_text(self.engine, f'Opening {target}')
            webbrowser.open(url)
            return True

        # say command: Jarvis echoes message
        m3 = re.match(r'say (.+)', cmd)
        if m3:
            msg = m3.group(1)
            speak_text(self.engine, msg)
            return True

        # fallback: echo and show help
        speak_text(self.engine, "I can try to open websites or search. Say 'help' for commands.")
        print("Unrecognized command:\n", cmd)
        return True

    def run(self):
        """Main loop: tries voice first, falls back to text input."""
        speak_text(self.engine, f'Hello, I am {self.name}. I am ready to assist. Say a command or type it in.')
        running = True
        while running:
            print('\nListening... (or type a command and press enter)') 
            command = safe_listen(self.recognizer)  # returns None on failure
            if command is None:
                # fallback to input
                try:
                    command = input('You (type): ').strip()
                except (KeyboardInterrupt, EOFError):
                    print('\nExiting...')
                    speak_text(self.engine, 'Goodbye.')
                    break
            else:
                print('You (voice):', command)

            running = self.handle_command(command)
