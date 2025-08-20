🚀 Complete Setup Guide for CHAOS AI Assistant
📋 Quick Checklist
 Python 3.7+ installed
 Repository cloned
 Dependencies installed
 API keys configured
 Microphone working
 Spotify account ready
🔧 Step-by-Step Installation
1. System Requirements
Operating System:

Windows 10/11 (recommended for full features)
macOS (limited system control)
Linux (limited system control)
Hardware:

Microphone for voice input
Speakers/headphones for audio output
Internet connection
2. Python Setup
Check Python version:

python --version
If Python not installed:

Download from python.org
During installation, check "Add Python to PATH"
3. Clone and Setup
# Clone repository
git clone https://github.com/yourusername/chaos-ai-assistant.git
cd chaos-ai-assistant

# Create virtual environment (recommended)
python -m venv chaos-env

# Activate virtual environment
# Windows:
chaos-env\Scripts\activate
# macOS/Linux:
source chaos-env/bin/activate

# Install dependencies
pip install -r requirements.txt
4. API Configuration
🤖 Google Gemini API
Get API Key:

Visit Google AI Studio
Click "Create API Key"
Copy the generated key
Add to config:

cp config_template.py config.py
Edit config.py:

apikey = "your_actual_api_key_here"
🎵 Spotify API
Create Spotify App:

Go to Spotify Developer Dashboard
Log in with your Spotify account
Click "Create App"
Fill in app details:
App name: "CHAOS AI Assistant"
App description: "Personal AI Assistant"
Redirect URI: https://open.spotify.com/
Get Credentials:

Copy Client ID and Client Secret
Add to config.py:
SPOTIFY_CLIENT_ID = "your_client_id_here"
SPOTIFY_CLIENT_SECRET = "your_client_secret_here"
5. Audio Setup
Windows
# If audio issues occur, install pyaudio separately
pip install pyaudio
macOS
# Install portaudio first
brew install portaudio
pip install pyaudio
Linux (Ubuntu/Debian)
sudo apt-get install python3-pyaudio
sudo apt-get install espeak espeak-data libespeak1 libespeak-dev
sudo apt-get install flac
6. First Run Test
python final.py
Expected output:

Welcome to CHAOS AI! Type 'exit' to quit or say 'exit' during audio input.
Type your command or say 'audio' for voice input:
>
🔍 Troubleshooting
Common Installation Issues
"No module named 'config'"
# Make sure you created config.py from template
cp config_template.py config.py
# Then edit config.py with your API keys
"Could not find PyAudio"
Windows:

pip install pipwin
pipwin install pyaudio
macOS:

brew install portaudio
pip install pyaudio
"pyttsx3 not working"
Linux:

sudo apt-get install espeak espeak-data libespeak1 libespeak-dev
macOS:

# Usually works out of the box, but if issues:
brew install espeak
"Speech recognition timeout"
Check microphone permissions
Adjust AUDIO_TIMEOUT in config.py
Test microphone with other apps first
Spotify Issues
"No active device found"
Open Spotify app on your device
Play any song briefly to activate device
Try CHAOS AI again
"Invalid client credentials"
Double-check Client ID and Secret in config.py
Ensure redirect URI is exactly: https://open.spotify.com/
Make sure app is not in development mode restrictions
"Insufficient permissions"
You need Spotify Premium for playback control
Free accounts can search but not control playback
🎯 Testing Your Setup
Basic Tests
Text Chat:

> hello
CHAOS: Hello! How can I help you today?
Voice Test:

> audio
CHAOS: Listening for up to 5 seconds.
[Say "hello"]
You said: hello
CHAOS: Hello! How can I help you today?
Web Test:

> open google.com
CHAOS: Opening google.
Time Test:

> what's the time
CHAOS: The time is 14:30:25.
Spotify Test:

> play despacito
CHAOS: Playing Despacito by Luis Fonsi.
🔒 Security Best Practices
Never share config.py

Keep API keys private

Regularly update dependencies:

pip install --upgrade -r requirements.txt
Monitor API usage on respective dashboards

🚀 Ready to Go!
If all tests pass, your CHAOS AI Assistant is ready to use!

Quick Start Commands:

python final.py - Start the assistant
audio - Switch to voice mode
exit - Quit the application
Enjoy your new AI assistant! 🎉
