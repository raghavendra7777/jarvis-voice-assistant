# jarvis-voice-assistant
A voice-enabled chatbot named Jarvis built for B.Tech final year hackathon projects. Jarvis listens to voice commands, speaks responses, and can open popular websites or perform Google searches. Built with SpeechRecognition, Pyttsx3, and Python. Includes text-mode fallback for environments without a microphone.
# 🎙️ Jarvis - Voice Assistant (Hackathon Project)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![SpeechRecognition](https://img.shields.io/badge/Library-SpeechRecognition-orange)](https://pypi.org/project/SpeechRecognition/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Jarvis** is a lightweight voice-enabled chatbot designed for **B.Tech final year hackathon projects**.  
It can listen to voice commands 🎤, speak responses 🔊, open popular websites 🌐, and perform quick Google searches.  

---

## 🚀 Features
- 🎤 **Voice input** (Google Speech Recognition via `speech_recognition`)  
- 🔊 **Text-to-speech output** (`pyttsx3`)  
- 🌐 **Open websites**: YouTube, Google, GitHub, Stack Overflow, Gmail, etc.  
- 🔍 **Search Google** with: `search for <query>`  
- 💬 **Echo command** with: `say <message>`  
- ⌨️ **Text-mode fallback** if no microphone is available  
- 🔧 Easy to extend for APIs, browser automation, or IoT  

---

## 📂 Project Structure
```bash
.
├── main.py        # Entry point
├── jarvis.py      # Core assistant logic
├── utils.py       # Helper functions (speech & TTS)
├── requirements.txt
└── README.md

