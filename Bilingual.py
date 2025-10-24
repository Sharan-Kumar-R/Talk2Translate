
import customtkinter as ctk
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os
import tempfile
import threading
import time
from tkinter import messagebox

# ---------------------------
# Helper: Play audio safely
# ---------------------------
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()

# ---------------------------
# Core Functionality
# ---------------------------
def translate_and_speak():
    r = sr.Recognizer()
    try:
        progressbar.start()
        start_button.configure(state="disabled")
        status_label.configure(text="🎤 Listening... Please speak now!", text_color="#4CAF50")
        root.update()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        lang_mode = mode_var.get()
        if lang_mode == "en-ta":
            text = r.recognize_google(audio, language="en-IN")
            status_label.configure(text=f"English: {text}", text_color="#2196F3")
            translated_text = GoogleTranslator(source='en', target='ta').translate(text)
            output_lang = 'ta'
        else:
            text = r.recognize_google(audio, language="ta-IN")
            status_label.configure(text=f"Tamil: {text}", text_color="#9C27B0")
            translated_text = GoogleTranslator(source='ta', target='en').translate(text)
            output_lang = 'en'

        output_text.configure(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("end", translated_text)
        output_text.configure(state="disabled")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts = gTTS(text=translated_text, lang=output_lang)
            tts.save(tmp_file.name)

        status_label.configure(text="🔊 Playing translation...", text_color="#FF9800")
        play_audio(tmp_file.name)
        os.remove(tmp_file.name)

        status_label.configure(text="✅ Done! Click 'Start Listening' again.", text_color="#4CAF50")

    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand audio.")
        status_label.configure(text="❌ Could not understand audio.", text_color="#E53935")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Speech recognition error: {e}")
        status_label.configure(text=f"⚠️ Request error: {e}", text_color="#E53935")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")
        status_label.configure(text=f"⚠️ Unexpected error: {e}", text_color="#E53935")
    finally:
        progressbar.stop()
        start_button.configure(state="normal")

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
# App Theme and Setup
# ---------------------------
ctk.set_appearance_mode("system")  # "dark", "light", or "system"
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("🎙 English ↔ Tamil Speech Translator")
root.geometry("600x460")
root.resizable(False, False)

# ---------------------------
# UI Layout
# ---------------------------
title_label = ctk.CTkLabel(root, text="🎙 English ↔ Tamil Speech Translator", font=("Segoe UI", 20, "bold"))
title_label.pack(pady=15)

mode_var = ctk.StringVar(value="en-ta")
mode_frame = ctk.CTkFrame(root)
mode_frame.pack(pady=10)

ctk.CTkLabel(mode_frame, text="Translation Mode:", font=("Segoe UI", 14)).pack(side="left", padx=8)
ctk.CTkRadioButton(mode_frame, text="English → Tamil", variable=mode_var, value="en-ta").pack(side="left", padx=10)
ctk.CTkRadioButton(mode_frame, text="Tamil → English", variable=mode_var, value="ta-en").pack(side="left", padx=10)

start_button = ctk.CTkButton(root, text="🎧 Start Listening", command=start_translation_thread, font=("Segoe UI", 15, "bold"), width=220, height=45)
start_button.pack(pady=15)

progressbar = ctk.CTkProgressBar(root, width=250)
progressbar.pack(pady=5)
progressbar.stop()

status_label = ctk.CTkLabel(root, text="Click 'Start Listening' to begin.", font=("Segoe UI", 13))
status_label.pack(pady=10)

output_text = ctk.CTkTextbox(root, height=130, width=480, font=("Segoe UI", 13))
output_text.pack(pady=10)
output_text.configure(state="disabled")

save_btn = ctk.CTkButton(root, text="💾 Save Translation", command=save_translation, width=160)
save_btn.pack(pady=5)


# Exit confirmation
def on_exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()
