from __future__ import annotations

import datetime
import os
import operator
import random
import sys
import time
import webbrowser
from pathlib import Path

import cv2
import pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from requests import get


# ============================================================
# JARVIS - Voice Assistant
# GitHub-safe version
# ============================================================

# Optional: set this environment variable to your music folder.
# Example on Windows:
#   set JARVIS_MUSIC_DIR=C:\Users\YourName\Music
MUSIC_DIR = Path(
    os.getenv("JARVIS_MUSIC_DIR", str(Path.home() / "Music"))
)


# ------------------------- Voice Engine -------------------------

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)


def speak(audio: str) -> None:
    """Speak text and also print it in the terminal."""
    print(f"JARVIS: {audio}")
    engine.say(audio)
    engine.runAndWait()


def take_command() -> str:
    """Listen to the microphone and convert speech to text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return "none"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )
        print(f"User: {query}")
        return query.lower()

    except sr.UnknownValueError:
        speak("Sorry sir, I could not understand that.")
        return "none"

    except sr.RequestError:
        speak("Sorry sir, the speech recognition service is unavailable.")
        return "none"


def wish() -> None:
    """Give a time-based greeting."""
    hour = datetime.datetime.now().hour

    if 0 <= hour <= 12:
        speak("Good morning sir.")
    elif 12 < hour < 18:
        speak("Good afternoon sir.")
    else:
        speak("Good evening sir.")

    speak("Please tell me how can I help you.")


# ------------------------- Helpers -------------------------

def open_chrome() -> None:
    """Open Google Chrome using the common Windows installation path."""
    chrome_paths = [
        Path(os.getenv("PROGRAMFILES", "")) /
        "Google/Chrome/Application/chrome.exe",
        Path(os.getenv("PROGRAMFILES(X86)", "")) /
        "Google/Chrome/Application/chrome.exe",
        Path(os.getenv("LOCALAPPDATA", "")) /
        "Google/Chrome/Application/chrome.exe",
    ]

    for path in chrome_paths:
        if path.exists():
            os.startfile(str(path))
            return

    webbrowser.open("https://www.google.com")


def calculate_expression() -> None:
    """Calculate a simple spoken expression such as '10 + 5'."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Ready.")
        print("Listening for calculation...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        expression = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower()

        print(f"Calculation: {expression}")

        parts = expression.split()

        if len(parts) != 3:
            speak("Please say an expression such as 10 plus 5.")
            return

        op1, oper, op2 = parts

        operator_map = {
            "+": operator.add,
            "plus": operator.add,
            "-": operator.sub,
            "minus": operator.sub,
            "x": operator.mul,
            "times": operator.mul,
            "*": operator.mul,
            "divided": operator.truediv,
            "/": operator.truediv,
        }

        if oper not in operator_map:
            speak("I do not support that operator.")
            return

        result = operator_map[oper](float(op1), float(op2))

        if result.is_integer():
            result = int(result)

        speak(f"Your result is {result}")

    except (sr.UnknownValueError, ValueError, ZeroDivisionError):
        speak("Sorry, I could not calculate that expression.")


def open_camera() -> None:
    """Open the webcam until the user presses ESC."""
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        speak("I could not access the camera.")
        return

    while True:
        ret, frame = camera.read()

        if not ret:
            break

        cv2.imshow("JARVIS Webcam - Press ESC to close", frame)

        if cv2.waitKey(50) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


# ------------------------- Main Program -------------------------

if __name__ == "__main__":
    wish()

    while True:
        query = take_command()

        if query == "none":
            continue

        # ---------------- Exit ----------------
        if "stop" in query or "go to sleep" in query:
            speak("Thank you sir. Goodbye.")
            sys.exit()

        # ---------------- Applications ----------------
        elif "open notepad" in query:
            os.startfile("notepad.exe")

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        # ---------------- Camera ----------------
        elif "open camera" in query:
            open_camera()

        # ---------------- Music ----------------
        elif "play music" in query:
            if not MUSIC_DIR.exists():
                speak(
                    "I could not find your music folder. "
                    "Set the JARVIS_MUSIC_DIR environment variable."
                )
                continue

            songs = [
                file for file in MUSIC_DIR.iterdir()
                if file.is_file()
            ]

            if not songs:
                speak("There are no music files in the configured folder.")
            else:
                selected_song = random.choice(songs)
                os.startfile(str(selected_song))
                speak(f"Playing {selected_song.stem}")

        # ---------------- Internet / Information ----------------
        elif "ip address" in query:
            try:
                ip = get("https://api.ipify.org", timeout=10).text
                speak(f"Your public IP address is {ip}")
            except Exception:
                speak("I could not retrieve your IP address.")

        elif "wikipedia" in query:
            topic = query.replace("wikipedia", "").strip()

            if not topic:
                speak("Please tell me what you want to search on Wikipedia.")
                continue

            try:
                speak("Searching Wikipedia sir. Give me some time.")
                results = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia.")
                speak(results)
            except Exception:
                speak("I could not find a Wikipedia result for that.")

        elif "open youtube" in query:
            speak("What would you like to watch?")
            search_query = take_command()

            if search_query != "none":
                pywhatkit.playonyt(search_query)

        elif "close youtube" in query:
            os.system("taskkill /f /im msedge.exe")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")

        elif "open takeuforward" in query:
            webbrowser.open("https://takeuforward.org")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")

        elif "open google" in query:
            speak("What should I search?")
            search_query = take_command()

            if search_query != "none":
                webbrowser.open(
                    "https://www.google.com/search?q="
                    + search_query.replace(" ", "+")
                )

        elif "google search" in query:
            search_query = query.replace("google search", "").strip()

            if search_query:
                webbrowser.open(
                    "https://www.google.com/search?q="
                    + search_query.replace(" ", "+")
                )

        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")

        elif "close google" in query:
            os.system("taskkill /f /im msedge.exe")

        # ---------------- WhatsApp ----------------
        elif "send message" in query:
            speak(
                "For safety, WhatsApp message sending is not hard-coded "
                "in this public version."
            )
            speak(
                "You can configure your own recipient and message workflow "
                "before enabling it."
            )

        # ---------------- System Controls ----------------
        elif "shut down the system" in query:
            speak("The system will shut down in five seconds.")
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            speak("The system will restart in five seconds.")
            os.system("shutdown /r /t 5")

        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {current_time}")

        # ---------------- Screenshot ----------------
        elif "take screenshot" in query:
            speak("Tell me a name for the file.")
            name = take_command()

            if name != "none":
                screenshot = pyautogui.screenshot()
                filename = f"{name.replace(' ', '_')}.png"
                screenshot.save(filename)
                speak(f"Screenshot saved as {filename}")

        # ---------------- Calculator ----------------
        elif "calculate" in query:
            calculate_expression()

        # ---------------- Volume ----------------
        elif "volume up" in query:
            for _ in range(5):
                pyautogui.press("volumeup")

        elif "volume down" in query:
            for _ in range(5):
                pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        # ---------------- Browser / Window Automation ----------------
        elif "refresh" in query:
            pyautogui.hotkey("ctrl", "r")

        elif "scroll down" in query:
            pyautogui.scroll(-1000)

        elif "who created you" in query:
            speak("I was created using Python by Anand.")

        elif "open chrome" in query:
            open_chrome()

        elif "maximize this window" in query:
            pyautogui.hotkey("alt", "space")
            time.sleep(1)
            pyautogui.press("x")

        elif "open new window" in query:
            pyautogui.hotkey("ctrl", "n")

        elif "open incognito window" in query:
            pyautogui.hotkey("ctrl", "shift", "n")

        elif "minimise this window" in query:
            pyautogui.hotkey("alt", "space")
            time.sleep(1)
            pyautogui.press("n")

        elif "open history" in query:
            pyautogui.hotkey("ctrl", "h")

        elif "open downloads" in query:
            pyautogui.hotkey("ctrl", "j")

        elif "previous tab" in query:
            pyautogui.hotkey("ctrl", "shift", "tab")

        elif "next tab" in query:
            pyautogui.hotkey("ctrl", "tab")

        elif "close tab" in query:
            pyautogui.hotkey("ctrl", "w")

        elif "close window" in query:
            pyautogui.hotkey("ctrl", "shift", "w")

        elif "clear browsing history" in query:
            pyautogui.hotkey("ctrl", "shift", "delete")

        else:
            speak("I don't have a command for that yet.")
