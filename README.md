# 🤖 JARVIS — Voice Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Voice%20Assistant-Automation-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Webcam-green?style=for-the-badge&logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/Windows-Desktop-blue?style=for-the-badge&logo=windows&logoColor=white">
</p>

<p align="center">
  <b>A Python-based voice-controlled desktop assistant for system automation, web interaction, information retrieval, and everyday desktop tasks.</b>
</p>

<p align="center">
  <a href="https://github.com/rudraa1069">
    <img src="https://img.shields.io/badge/GitHub-rudraa1069-black?style=for-the-badge&logo=github">
  </a>
  <a href="https://www.linkedin.com/in/anand-kr-choudhary">
    <img src="https://img.shields.io/badge/LinkedIn-Anand%20Choudhary-blue?style=for-the-badge&logo=linkedin">
  </a>
</p>

---

## 🧠 About the Project

**JARVIS** is a Python-based voice assistant that allows users to interact with their computer using spoken commands.

The assistant listens through the microphone, converts speech into text, interprets the command, and performs the corresponding action.

The project combines:

- 🎙️ Speech Recognition
- 🔊 Text-to-Speech
- 🖥️ Windows System Automation
- 🌐 Web Automation
- 📚 Information Retrieval
- 📷 Webcam Control
- 📸 Screenshot Automation
- 🧮 Voice-Based Calculations

---

## ✨ Features

### 🎙️ Voice Interaction

- Voice command recognition
- Text-to-speech responses
- Time-based greetings
- Handles unrecognized speech
- Handles speech-recognition service errors

### 🖥️ System Automation

JARVIS can control several Windows operations through voice commands:

- Open / close Notepad
- Open / close Command Prompt
- Open Chrome
- Maximize / minimize windows
- Open new browser window
- Open incognito window
- Open browser history
- Open downloads
- Switch browser tabs
- Close tabs/windows
- Lock the computer
- Restart the computer
- Shut down the computer

### 🌐 Web & Information

JARVIS can:

- Search Google
- Search Wikipedia
- Play YouTube content
- Open websites
- Retrieve the public IP address
- Open predefined websites

### 🎵 Multimedia

- Play random music from a configured local music directory
- Control system volume
- Mute system audio
- Access the webcam

### 🧰 Productivity

- Take screenshots
- Perform simple voice-based calculations
- Scroll webpages
- Refresh webpages
- Automate keyboard shortcuts

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Speech-to-text |
| pyttsx3 | Text-to-speech |
| OpenCV | Webcam access |
| PyAutoGUI | Keyboard, mouse and screenshot automation |
| PyWhatKit | Web/YouTube automation |
| Wikipedia | Information retrieval |
| Requests | Public IP lookup |
| Webbrowser | Browser automation |

---

## 🔄 How JARVIS Works
---

## 📸 Screenshots

### 🎙️ JARVIS Voice Assistant

<p align="center">
  <img src="Screenshot%202026-10-08%20135252.png" width="900">
</p>

### 🖥️ JARVIS Running in Terminal

<p align="center">
  <img src="Screenshot%202026-10-08%20135303.png" width="900">
</p>

---

```text
                 🎙️ User Voice
                      │
                      ▼
             ┌──────────────────┐
             │ Speech Recognition│
             └────────┬─────────┘
                      │
                      ▼
                🧠 Command
                  Processing
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      🖥️ System     🌐 Web      🧰 Utility
      Commands     Commands     Commands
          │           │           │
          └───────────┼───────────┘
                      ▼
                ⚙️ Action
                 Executed
                      │
                      ▼
                🔊 Response
