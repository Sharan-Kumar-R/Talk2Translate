<h1 align="center">🎙 English ↔ Tamil Speech Translator</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-FFD43B?style=for-the-badge&logo=python&logoColor=306998" alt="Python">
  <img src="https://img.shields.io/badge/speechrecognition-1E90FF?style=for-the-badge&logo=python&logoColor=white" alt="SpeechRecognition">
  <img src="https://img.shields.io/badge/deep-translator-32CD32?style=for-the-badge&logo=google&logoColor=white" alt="Deep Translator">
  <img src="https://img.shields.io/badge/gtts-FF4500?style=for-the-badge&logo=soundcloud&logoColor=white" alt="gTTS">
  <img src="https://img.shields.io/badge/pygame-FF1493?style=for-the-badge&logo=pygame&logoColor=white" alt="Pygame">
  <img src="https://img.shields.io/badge/multilingual-8A2BE2?style=for-the-badge&logo=googletranslate&logoColor=white" alt="English-Tamil">
</p>

A real-time speech translation application that converts spoken English to Tamil and vice versa, with text-to-speech playback functionality.

## Features

-  Speak in English or Tamil and get instant translation.
-  Automatic bidirectional translation (English ↔ Tamil).
-  Listen to the translated speech output.
-  Save Translations - Store your translations to a local file
-  Clean, modern UI using CustomTkinter.
-  Threaded processing for smooth performance.


##  Prerequisites

Before running this application, ensure you have:

- Python 3.7 or higher
- A working microphone
- Internet connection (required for speech recognition and translation APIs)
- Audio output device for playback
  
##  Installation

1.  **Clone the repository (or download the script):**
    ```bash
    git clone https://github.com/Sharan-Kumar-R/Talk2Translate.git
    cd speech-translator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    If you don't have a `requirements.txt` file, you can create one or install them individually:
    ```bash
    pip install customtkinter SpeechRecognition deep-translator gTTS pygame
    ```

4.  **Install PortAudio:** `SpeechRecognition`'s `PyAudio` dependency (which is used for microphone input) requires PortAudio.
    *   **On macOS:**
        ```bash
        brew install portaudio
        ```
    *   **On Windows:** Download pre-compiled wheels for `PyAudio` from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) (search for PyAudio) and install using pip, e.g., `pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl`. Alternatively, you might need to install C++ build tools for Visual Studio.
    *   **On Linux (Debian/Ubuntu):**
        ```bash
        sudo apt-get install portaudio19-dev python3-pyaudio
        ```

##  Usage

1. **Run the application**
```bash
python Bilingual.py
```

2. **Select Translation Mode**
   - Choose "English → Tamil" to speak in English
   - Choose "Tamil → English" to speak in Tamil

3. **Start Listening**
   - Click the "🎧 Start Listening" button
   - Speak clearly into your microphone
   - Wait for the translation to appear

4. **Save Translations**
   - Click "💾 Save Translation" to save the current translation
   - Translations are saved to `translations.txt` in the application directory

##  How It Works

1. **Speech Capture**: The application listens to your microphone input
2. **Speech-to-Text**: Converts your speech to text using Google Speech Recognition
3. **Translation**: Translates the text using Google Translator
4. **Text-to-Speech**: Converts the translated text to speech
5. **Playback**: Plays the audio translation automatically

##  Project Structure
```
Talk2Translate/
│
├── Bilingual.py          # Main application file
├── requirements.txt       # Python dependencies
├── translations.txt       # Saved translations (auto-generated)
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

In case of any queries, please leave a message or contact me via the email provided in my profile.

<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>



















