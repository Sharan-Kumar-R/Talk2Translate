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

## Demo / Output

The application provides a user-friendly graphical interface for real-time voice translation:

<p align="center">
  <img src="https://github.com/Sharan-Kumar-R/Talk2Translate/blob/main/Talk2Translate.png" alt="Talk2Translate Interface" width="600">
</p>

##  Prerequisites

Before running this application, ensure you have:

- Python 3.7 or higher
- A working microphone
- Internet connection (required for speech recognition and translation APIs)
- Audio output device for playback
  
## Installation

### Step 1: Clone the Repository

**Option A: Using VS Code Terminal**
1. Open Visual Studio Code
2. Open a new terminal (Terminal → New Terminal or `Ctrl+Shift+``)
3. Navigate to your desired directory:
```bash
   cd path/to/your/desired/folder
```
4. Clone the repository:
```bash
   git clone https://github.com/Sharan-Kumar-R/Talk2Translate.git
```
5. Open the project folder:
```bash
   cd Talk2Translate
```
6. Open the project in VS Code:
```bash
   code .
```

**Option B: Using VS Code Git Integration**
1. Open Visual Studio Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "Git: Clone" and select it
4. Paste the repository URL: `https://github.com/Sharan-Kumar-R/Talk2Translate.git`
5. Choose a folder location and click "Select Repository Location"
6. Click "Open" when prompted

### Step 2: Create a Virtual Environment (Recommended)

1. In the VS Code terminal, create a virtual environment:
```bash
   python -m venv venv
```

2. Activate the virtual environment:
   - **Windows:**
```bash
     venv\Scripts\activate
```
   - **macOS/Linux:**
```bash
     source venv/bin/activate
```

### Step 3: Install Python Dependencies

Install the required packages:
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, install packages individually:
```bash
pip install customtkinter SpeechRecognition deep-translator gTTS pygame
```

### Step 4: Install PortAudio (Required for Microphone Input)

The `SpeechRecognition` library requires PortAudio for microphone functionality.

**macOS:**
```bash
brew install portaudio
```

**Windows:**
1. Download the appropriate PyAudio wheel file from [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
2. Install using pip:
```bash
   pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

Alternatively, install Microsoft C++ Build Tools if needed.

**Linux (Debian/Ubuntu):**
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
























