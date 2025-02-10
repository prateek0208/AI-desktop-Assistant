import datetime
import threading
import webbrowser
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyautogui
import time
from config import apikey

# Configure Google Gemini
genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Ensure the speech engine uses the right voice and settings
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose the first voice, or use voices[1].id for another voice
engine.setProperty('rate', 150)  # Set speech rate (optional)
engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)


# Function to speak text with interrupt handling
def speak(text):
    try:
        print(f"CHAOS: {text}")  # Debugging: Output text being spoken
        engine.say(text)
        engine.runAndWait()  # Run the event loop until speech is done
    except Exception as e:
        print(f"Error in TTS: {e}")


# Function to log conversations
def log_conversation(query, response):
    log_file = "conversation_log.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] User: {query}\n")
        file.write(f"[{timestamp}] CHAOS: {response}\n\n")


# Function to process chat queries
chatStr = ""  # Initialize global conversation history


def chat(query):
    global chatStr
    # Append new user input to conversation history
    chatStr += f"User: {query}\n---\n"

    try:
        response = model.generate_content(chatStr)  # Use full chat history
        response_text = response.text
        # Append AI response to conversation history
        chatStr += f"{response_text}\n---\n"
        log_conversation(query, response_text)  # Log interaction
        return response_text

    except Exception as e:
        error_msg = f"Sorry, I couldn't process the request at the moment: {e}"
        # Append error message to history
        chatStr += f" {error_msg}\n---\n"
        log_conversation(query, error_msg)
        return error_msg


# Function to handle audio input
def audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for up to 5 seconds.")
        try:
            audio = recognizer.listen(source, timeout=3)
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
        return None


# Function to get the current time
def get_time():
    now = datetime.datetime.now()
    response = f"The time is {now.strftime('%H:%M:%S')}."
    speak(response)
    return response


# Function to play a song
def play_song(query):
    song_name = query.replace("play", "").strip()
    print(f"Searching for: {song_name}")

    if not song_name:
        speak("Please specify a song name.")
        return

    try:
        # Set up the Spotify client
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="9786556b4b334d7188e3d82eda591603",
            client_secret="b5ba5328afe04e2eb9841158cf34d9c2",
            redirect_uri="https://open.spotify.com/",
            scope="user-library-read user-read-playback-state user-modify-playback-state"))

        # Search for the song
        results = sp.search(q=song_name, limit=1, type='track')
        print(f"Spotify search results: {results}")

        if not results['tracks']['items']:
            speak(f"Sorry, I couldn't find the song '{song_name}'.")
            return

        track = results['tracks']['items'][0]
        print(f"Found {track['name']} by {track['artists'][0]['name']}. Trying to play it...")

        # List available devices
        devices = sp.devices()
        print(f"Devices found: {devices['devices']}")

        # Try to find an active device or use the first available one
        active_device = next((device for device in devices['devices'] if device['is_active']), None)
        if not active_device and devices['devices']:
            active_device = devices['devices'][0]

        if not active_device:
            speak("No active or available device found. Please make sure Spotify is open on a device.")
            return

        # Start playback
        sp.start_playback(uris=[track['uri']], device_id=active_device['id'])
        print("Playback started.")

        # Check playback state with retries
        for _ in range(3):
            current_playback = sp.current_playback()
            if current_playback and current_playback['is_playing']:
                speak(f"Playing {track['name']} by {track['artists'][0]['name']}.")
                return
            else:
                print("Waiting for playback to start...")
                time.sleep(2)

        speak(f"Failed to start playback of {track['name']} by {track['artists'][0]['name']}.")

    except spotipy.exceptions.SpotifyException as e:
        print(f"Spotify API error: {e}")
        speak("There was an issue with Spotify's API.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        speak("An unexpected error occurred.")


# Function to open websites
def open_website(query):
    site_name = query.replace("open", "").replace("site", "").strip()
    site_name_call = site_name
    if site_name:
        if not site_name.startswith("http"):
            if "." not in site_name:
                site_name = f"{site_name}.com"
            site_name = f"https://{site_name}"

        try:
            webbrowser.open(site_name)
            print(f"{site_name}")
            response = f"Opening {site_name_call}."
            speak(response)
            return response
        except Exception as e:
            error_msg = f"Sorry, I couldn't open the website. Error: {e}"
            print(error_msg)
            speak(error_msg)
            return error_msg
    else:
        response = "Sorry, I couldn't understand the website you want to open. Please specify a valid site."
        speak(response)
        return response


# Function to launch an app using the Start Menu
def launch_app_in_background(app_name):
    def launch_app():
        try:
            pyautogui.press('win')
            time.sleep(0.5)
            pyautogui.write(app_name, interval=0.1)
            time.sleep(1)
            pyautogui.press('enter')
            print(f"CHAOS: Attempting to launch {app_name}.")
        except Exception as e:
            print(f"Error launching {app_name}: {e}")

    thread = threading.Thread(target=launch_app)
    thread.daemon = True
    thread.start()


def extract_app_name(input_text):
    keywords = ["open", "launch", "from the start menu", "start", "execute"]
    for keyword in keywords:
        input_text = input_text.replace(keyword, "").strip()
    return input_text


# Main loop
if __name__ == "__main__":
    print("Welcome to CHAOS AI! Type 'exit' to quit or say 'exit' during audio input.")
    while True:
        try:
            print("Type your command or say 'audio' for voice input:")
            command = input("> ").strip().lower()

            if command == "exit":
                speak("Goodbye!")
                break

            if command == "audio":
                user_query = audio_input()
                if not user_query:
                    continue

                if "exit" in user_query.lower():
                    print("Goodbye!")
                    speak("Goodbye!")
                    break
                process_query = user_query
            else:
                process_query = command

            # Handle other commands
            if "open" in process_query or "launch" in process_query:
                if "site" in process_query or ".com" in process_query or ".org" in process_query:
                    open_website(process_query)
                else:
                    app_name = extract_app_name(process_query)
                    if app_name:
                        launch_app_in_background(app_name)
                    else:
                        speak("I couldn't identify the application name.")
            elif "search for" in process_query and "on the browser" in process_query:
                search_query = process_query.replace("search for", "").replace("on the browser", "").strip()
                if search_query:
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
                    response = f"Searching for {search_query} on the browser."
                    speak(response)
                else:
                    speak("I couldn't understand what to search for.")
            elif "play" in process_query and "song" in process_query:
                play_song(process_query)
            elif "the time" in process_query:
                get_time()
            else:
                # Fallback to general chat handling
                response = chat(process_query)
                speak(response)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred. Please try again.")
