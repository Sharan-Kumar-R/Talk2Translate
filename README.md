<h1 align="center">🎙 English ↔ Tamil Speech Translator (Ollama LLM)</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-FFD43B?style=for-the-badge&logo=python&logoColor=306998" alt="Python">
  <img src="https://img.shields.io/badge/speechrecognition-1E90FF?style=for-the-badge&logo=python&logoColor=white" alt="SpeechRecognition">
  <img src="https://img.shields.io/badge/ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/llama3.2-8B4513?style=for-the-badge&logo=meta&logoColor=white" alt="Llama 3.2">
  <img src="https://img.shields.io/badge/gtts-FF4500?style=for-the-badge&logo=soundcloud&logoColor=white" alt="gTTS">
  <img src="https://img.shields.io/badge/pygame-FF1493?style=for-the-badge&logo=pygame&logoColor=white" alt="Pygame">
  <img src="https://img.shields.io/badge/multilingual-8A2BE2?style=for-the-badge&logo=googletranslate&logoColor=white" alt="English-Tamil">
</p>

A real-time speech translation application that converts spoken English to Tamil and vice versa, powered by **Ollama's local LLM (Llama 3.2)** for translation, with text-to-speech playback functionality.

##  Features

-  Speak in English or Tamil and get instant translation
-  **Local LLM-powered translation** using Ollama (Llama 3.2)
-  Automatic bidirectional translation (English ↔ Tamil)
-  Listen to the translated speech output
-  Save Translations - Store your translations to a local file
-  Clean, modern UI using CustomTkinter
-  Threaded processing for smooth performance
-  **Privacy-focused** - All translation happens locally

##  What's New - Ollama Integration

This version replaces cloud-based translation APIs with **local LLM translation** using Ollama:

-  **100% offline translation** (after initial model download)
-  **No API costs** or rate limits
-  **Enhanced privacy** - your data never leaves your machine
-  **Customizable** - Easy to switch between different Ollama models
-  **High-quality translations** powered by Llama 3.2

## 📸 Demo / Output

The application provides a user-friendly graphical interface for real-time voice translation:

<p align="center">
  <img src="https://github.com/Sharan-Kumar-R/Talk2Translate/blob/main/Talk2Translate.png" alt="Talk2Translate Interface" width="500">
</p>

##  Prerequisites

Before running this application, ensure you have:

- Python 3.7 or higher
- A working microphone
- Audio output device for playback
- **Ollama installed and running locally** (see installation steps below)
- Internet connection (only for initial Ollama model download and speech recognition)

##  Installation

### Step 1: Install Ollama

**Ollama is required for local LLM-based translation.**

1. Visit [ollama.com](https://ollama.com) and download the installer for your OS
2. Install Ollama following the platform-specific instructions:
   - **Windows**: Run the installer
   - **macOS**: Drag to Applications folder
   - **Linux**: Follow the command line installation

3. Verify Ollama installation:
```bash
ollama --version
```

4. Pull the Llama 3.2 model (used by default):
```bash
ollama pull llama3.2:latest
```

5. Start the Ollama server (if not already running):
```bash
ollama serve
```

**Note:** The Ollama server should be running at `http://localhost:11434` (default). The application will connect to this endpoint.

### Step 2: Clone the Repository

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

### Step 3: Create a Virtual Environment (Recommended)

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

### Step 4: Install Python Dependencies

Install the required packages:
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, install packages individually:
```bash
pip install customtkinter SpeechRecognition gTTS pygame ollama
```

### Step 5: Install PortAudio (Required for Microphone Input)

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

### 1. Start Ollama Server (if not already running)
```bash
ollama serve
```

### 2. Run the Application
```bash
python Bilingual.py
```

### 3. Select Translation Mode
- Choose "English → Tamil" to speak in English
- Choose "Tamil → English" to speak in Tamil

### 4. Start Listening
- Click the "🎧 Start Listening" button
- Speak clearly into your microphone
- Wait for the LLM translation to appear

### 5. Save Translations
- Click "💾 Save Translation" to save the current translation
- Translations are saved to `translations.txt` in the application directory

##  Configuration

You can customize the Ollama configuration by editing these variables in `Bilingual.py`:
```python
OLLAMA_HOST = "http://localhost:11434"  # Ollama server address
OLLAMA_MODEL = "llama3.2:latest"        # Model to use for translation
```

### Available Ollama Models for Translation

You can experiment with different models:
```bash
# Smaller, faster model
ollama pull llama3.2:1b

# Default model (balanced)
ollama pull llama3.2:latest

# Larger, more capable model
ollama pull llama3.1:8b

# Or other multilingual models
ollama pull mistral
```

Update the `OLLAMA_MODEL` variable in the code to switch models.

##  How It Works

1. **Speech Capture**: The application listens to your microphone input
2. **Speech-to-Text**: Converts your speech to text using Google Speech Recognition
3. **LLM Translation**: Translates the text using local Ollama LLM (Llama 3.2)
4. **Text-to-Speech**: Converts the translated text to speech using gTTS
5. **Playback**: Plays the audio translation automatically

##  Project Structure
```
Talk2Translate/
│
├── Bilingual.py          # Main application file (uses google translator)
├── Bilingualllm.py       # Main application file (uses local llm)
├── Talk2Translate.png    # Demo image
├── requirements.txt      # Python dependencies
├── translations.txt      # Saved translations (auto-generated)
└── README.md             # This file
```


##  Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

In case of any queries, please leave a message or contact me via the email provided in my profile.


<p align="center">
⭐ <strong>Star this repository if you found it helpful!</strong>
</p>






