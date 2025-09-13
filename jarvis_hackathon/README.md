# Jarvis - Voice Web Assistant (Hackathon Demo)

**Jarvis** is a lightweight voice-enabled chatbot designed as a B.Tech final year hackathon project demo. It listens to voice commands, speaks responses, and can open websites or run quick searches via your default web browser.

## 🚀 Features
- Voice input (uses Google Speech Recognition via `speech_recognition`)
- Text-to-speech output (`pyttsx3`)
- Open websites (YouTube, Google, GitHub, Stack Overflow, etc.)
- Search Google for phrases: `search for <query>`
- Text-mode fallback for environments without a microphone
- Easy to extend for more custom actions (API calls, browser automation, etc.)

## 📁 Files
- `main.py` - Entry point (starts Jarvis)
- `jarvis.py` - Main assistant logic and command handling
- `utils.py` - Helper functions for speech input and TTS
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## ⚙️ Setup (Recommended for hackathon demo)
1. Create a Python 3.8+ virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Jarvis:
   ```bash
   python main.py
   ```
4. Try voice commands like:
   - `open youtube`
   - `search for machine learning tutorials`
   - `open stack overflow`
   - `say hello jarvis`
   - `help`

## 🧠 Extending for Hackathon (Ideas)
- Integrate a proper conversational model (OpenAI/Gemini or Hugging Face) for richer responses.
- Add browser automation with `selenium` for logged-in tasks (e.g., post to LinkedIn).
- Add command scheduling, reminders, or simple IoT control (if hardware available).
- Add a React or Electron front-end for a polished demo UI.

## 🔒 Notes & Safety
- The script uses Google’s free speech-to-text via `speech_recognition` which requires internet access.
- For stable image or model-based responses, you may need API keys (not included).
- Be careful running untrusted code or opening URLs automatically; review and change any commands as needed.

## 📜 License
MIT License
