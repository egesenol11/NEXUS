# 🎙️ NEXUS - Intelligent Personal Voice Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<div align="center">
  <img src="nexusGitLogo.png" alt="Nexus Logo" width="150" height="150">
  <br>
  <i>"Your voice is my command."</i>
</div>
[![Download on itch.io]](https://egesenol11.itch.io/nexus)

## 📖 Overview
**NEXUS** is a lightweight, Python-based desktop voice assistant designed to automate daily tasks, control media, and manage system operations. Unlike standard assistants, NEXUS features a **dynamic noise cancellation system** and a **minimalist, auto-cleaning GUI** that keeps your screen distraction-free.

This project demonstrates the use of **Speech Recognition**, **Threaded Processes**, and **GUI Automation** in a real-world application.

## 🚀 Key Features
* **Smart Wake-Word Detection:** Understands "Nexus" and tolerates phonetic variations (e.g., "Next", "Meksis", "Mesut") for high responsiveness.
* **Dynamic Microphone Calibration:** Automatically adjusts energy threshold based on ambient noise at startup.
* **Minimalist UI:** Features a sleek, dark-themed interface that displays commands only when active and auto-clears history to maintain a clean look.
* **App Integration:** Direct voice control for **WhatsApp**, **Steam**, **Spotify**, and specific games (NBA 2K26, ETS 2, etc.).
* **Smart Contact Search:** Can find contacts in the directory and initiate Voice/Video calls or open chats via WhatsApp Desktop.

## 🛠️ Technologies Used
* **SpeechRecognition:** For converting audio to text (Google Speech API).
* **PyAutoGUI:** For simulating keyboard/mouse actions and screenshots.
* **Tkinter:** For the graphical user interface (GUI).
* **Pyttsx3:** For offline text-to-speech feedback.
* **Threading:** To run the listening loop without freezing the GUI.

## 📦 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/egesenol11/NEXUS.git](https://github.com/egesenol11/NEXUS.git)
    cd NEXUS
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a requirements file, install these manually: `pip install SpeechRecognition pyttsx3 pyautogui pyaudio`)*

3.  **Run the Assistant**
    ```bash
    python nexus.py
    ```

## 🗣️ Voice Commands (Türkçe)

NEXUS understands **Turkish** and **English** (can switch modes). Here are the core commands:

### 🟢 System & Utilities
* **"Nexus"** (or "Hey", "Sistem"): Wakes up the assistant.
* **"Türkçe konuş" / "Speak English":** Switches the language mode.
* **"Saat kaç?":** Tells the current time.
* **"Kapat" / "Shutdown":** Shuts down the PC (Can specify time: *"30 dakika sonra kapat"*).
* **"SS al" / "Fotoğraf":** Takes a screenshot.

### 🎮 Apps & Games
* **"Steam aç":** Launches Steam.
* **"NBA başlat":** Launches NBA 2K26.
* **"ETS aç" / "Truck":** Launches Euro Truck Simulator 2.
* **"Google aç":** Opens Google in the browser.

### 📱 Communication (WhatsApp)
* **"WhatsApp aç":** Opens the app.
* **"[İsim] ara":** Starts a WhatsApp voice call with the person.
* **"[İsim] görüntülü ara":** Starts a video call.
* **"[İsim] mesaj":** Opens the chat window for the person.

### 🎵 Media Control
* **"Başlat" / "Spotify":** Opens Spotify and plays music.
* **"Durdur":** Pauses the media.
* **"Değiştir" / "Sıradaki":** Skips to the next track.

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

---
<div align="center">
  Developed with ❤️ by <a href="https://github.com/egesenol11">Ege Şenol</a>
</div>
