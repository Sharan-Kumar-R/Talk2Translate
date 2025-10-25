import os
import tempfile
import threading
import time
from tkinter import messagebox
import customtkinter as ctk
import speech_recognition as sr
from gtts import gTTS
import pygame # Make sure pygame is imported

# ---------------------------
# Ollama SDK setup
# ---------------------------
import ollama # Import ollama client library

# ---------------------------
# Ollama Configuration
# ---------------------------
OLLAMA_HOST = "http://localhost:11434" # Default Ollama server address
OLLAMA_MODEL = "llama3.2:latest" # <<< CURRENTLY USING LLAMA3.2:LATEST

# ---------------------------
# Helper: Play audio safely
# ---------------------------
def play_audio(file_path):
    print(f"Attempting to play audio from: {file_path}")
    try:
        if not pygame.mixer.get_init(): # Check if mixer is already initialized
            pygame.mixer.init()
            print("pygame mixer initialized.")
        else:
            print("pygame mixer already initialized.")

        if not os.path.exists(file_path):
            print(f"Error: Audio file not found at {file_path}")
            messagebox.showerror("Audio Error", f"Audio file not found: {os.path.basename(file_path)}")
            return

        pygame.mixer.music.load(file_path)
        print("pygame mixer loaded music.")
        pygame.mixer.music.play()
        print("pygame mixer started playback.")

        # Wait for playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        print("pygame mixer finished playback.")

    except pygame.error as e:
        print(f"Pygame mixer error: {e}")
        messagebox.showerror("Audio Error", f"Could not play audio. Pygame error: {e}\n"
                                             "Please check your sound device and drivers.")
    except Exception as e:
        print(f"Unexpected error during audio playback: {e}")
        messagebox.showerror("Audio Error", f"An unexpected error occurred during audio playback: {e}")
    finally:
        if pygame.mixer.get_init():
            pygame.mixer.quit() # Always quit the mixer to release resources
            print("pygame mixer quit.")

# ---------------------------
# LLM-based translation using Ollama
# ---------------------------
def llm_translate_via_ollama(text: str, src_label: str, tgt_label: str, model: str = OLLAMA_MODEL) -> str:
    """
    Use a local Ollama LLM to perform translation.
    """
    system_msg = (
        "You are a highly accurate and professional translation assistant. "
        "Your task is to translate sentences from one language to another with utmost precision, "
        "preserving the exact meaning, tone, and grammatical structure. "
        "Do NOT add any extra commentary, explanations, or conversational filler. "
        "Only provide the translated text. Be concise and accurate. "
        "If an input phrase is already in the target language or cannot be meaningfully translated, "
        "restate it as-is or provide the most direct equivalent."
    )
    user_msg = f"Translate the following from {src_label} to {tgt_label}:\n\n{text}"

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            options={
                "temperature": 0.0,
                "num_ctx": 4096,
            }
        )

        translated_text = response['message']['content'].strip()
        return translated_text

    except Exception as e:
        raise RuntimeError(f"Ollama LLM API call error: {e}. "
                           f"Ensure Ollama server is running, model '{model}' is downloaded, "
                           f"and connection to {OLLAMA_HOST} is possible.")

# ---------------------------
# Core Functionality: STT → LLM → TTS
# (Modified to call llm_translate_via_ollama)
# ---------------------------
def translate_and_speak():
    recognizer = sr.Recognizer()
    temp_mp3_file = None # Initialize to None

    try:
        progressbar.start()
        start_button.configure(state="disabled")
        status_label.configure(text="Listening... Please speak now.", text_color="#4CAF50")
        root.update()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=12)

        lang_mode = mode_var.get()
        if lang_mode == "en-ta":
            text = recognizer.recognize_google(audio, language="en-IN")
            status_label.configure(text=f"English: {text}", text_color="#2196F3")
            src_label, tgt_label, tts_lang = "English", "Tamil", "ta"
        else:
            text = recognizer.recognize_google(audio, language="ta-IN")
            status_label.configure(text=f"Tamil: {text}", text_color="#9C27B0")
            src_label, tgt_label, tts_lang = "Tamil", "English", "en"

        root.update()

        try:
            translated_text = llm_translate_via_ollama(text, src_label, tgt_label)
        except Exception as e:
            messagebox.showerror("Translation error", f"Translation failed: {e}")
            status_label.configure(text=f"Translation failed: {e}", text_color="#E53935")
            progressbar.stop()
            start_button.configure(state="normal")
            return

        output_text.configure(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("end", translated_text)
        output_text.configure(state="disabled")

        print(f"Attempting gTTS for: '{translated_text}' in language '{tts_lang}'")
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                temp_mp3_file = tmp_file.name # Store file path for later deletion
                tts = gTTS(text=translated_text, lang=tts_lang)
                tts.save(temp_mp3_file)
            print(f"gTTS successfully saved to {temp_mp3_file}")
        except Exception as tts_e:
            messagebox.showerror("Text-to-Speech Error", f"Failed to generate speech: {tts_e}\n"
                                                           "Check network connection and gTTS installation.")
            print(f"Error generating gTTS: {tts_e}")
            status_label.configure(text=f"Text-to-Speech failed: {tts_e}", text_color="#E53935")
            return # Stop here if TTS fails

        status_label.configure(text="Playing translation...", text_color="#FF9800")
        root.update() # Update UI to show playing status
        play_audio(temp_mp3_file)

        status_label.configure(text="Done. Click 'Start Listening' again.", text_color="#4CAF50")

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio.")
        status_label.configure(text="Could not understand audio.", text_color="#E53935")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Speech recognition error: {e}")
        status_label.configure(text=f"Speech recognition error: {e}", text_color="#E53935")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")
        status_label.configure(text=f"Unexpected error: {e}", text_color="#E53935")
    finally:
        progressbar.stop()
        start_button.configure(state="normal")
        if temp_mp3_file and os.path.exists(temp_mp3_file):
            try:
                os.remove(temp_mp3_file)
                print(f"Cleaned up temporary file: {temp_mp3_file}")
            except OSError as e:
                print(f"Error removing temporary file {temp_mp3_file}: {e}")


# ---------------------------
# Thread Wrapper
# ---------------------------
def start_translation_thread():
    threading.Thread(target=translate_and_speak, daemon=True).start()

# ---------------------------
# Save Translation
# ---------------------------
def save_translation():
    text = output_text.get("1.0", "end").strip()
    if not text:
        messagebox.showinfo("Empty", "No translation to save yet.")
        return
    with open("translations.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n\n")
    messagebox.showinfo("Saved", "Translation saved to translations.txt")

# ---------------------------
# App Theme and Setup (UI)
# ---------------------------
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("English ↔ Tamil Speech Translator (Ollama LLM - Llama 3.2)") # Updated title for clarity
root.geometry("600x460")
root.resizable(False, False)

title_label = ctk.CTkLabel(root, text="English ↔ Tamil Speech Translator (Ollama LLM - Llama 3.2)", font=("Segoe UI", 20, "bold"))
title_label.pack(pady=15)

# --- Ollama Model Display (New) ---
ollama_model_label = ctk.CTkLabel(root, text=f"Ollama Model: {OLLAMA_MODEL} (Host: {OLLAMA_HOST})", font=("Segoe UI", 10), text_color="gray")
ollama_model_label.pack(pady=(0, 5))
# -----------------------------------

mode_var = ctk.StringVar(value="en-ta")
mode_frame = ctk.CTkFrame(root)
mode_frame.pack(pady=10)

ctk.CTkLabel(mode_frame, text="Translation Mode:", font=("Segoe UI", 14)).pack(side="left", padx=8)
ctk.CTkRadioButton(mode_frame, text="English → Tamil", variable=mode_var, value="en-ta").pack(side="left", padx=10)
ctk.CTkRadioButton(mode_frame, text="Tamil → English", variable=mode_var, value="ta-en").pack(side="left", padx=10)

start_button = ctk.CTkButton(root, text="Start Listening", command=start_translation_thread, font=("Segoe UI", 15, "bold"), width=220, height=45)
start_button.pack(pady=15)

progressbar = ctk.CTkProgressBar(root, width=250)
progressbar.pack(pady=5)
progressbar.stop()

status_label = ctk.CTkLabel(root, text="Click 'Start Listening' to begin.", font=("Segoe UI", 13))
status_label.pack(pady=10)

output_text = ctk.CTkTextbox(root, height=130, width=480, font=("Segoe UI", 13))
output_text.pack(pady=10)
output_text.configure(state="disabled")

save_btn = ctk.CTkButton(root, text="Save Translation", command=save_translation, width=160)
save_btn.pack(pady=5)

def on_exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()