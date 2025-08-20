CHAOS AI Assistant 🤖
A powerful voice-activated AI assistant built with Python that combines Google Gemini AI, Spotify integration, and system control capabilities.

✨ Features
Voice Recognition: Speak naturally to control your computer
AI Conversations: Powered by Google Gemini 1.5 Flash
Music Control: Play songs directly from Spotify
System Control: Manage applications, volume, and system functions
Web Navigation: Open websites and perform web searches
Persistent Memory: Remembers conversation context
Text-to-Speech: Natural voice responses
🎯 Capabilities
🗣️ Voice Commands
"Play [song name]" - Play music from Spotify
"Open [website/application]" - Launch apps or websites
"Close [application]" - Terminate running applications
"Search for [query] on the browser" - Web search
"What's the time?" - Get current time
"Increase/decrease volume" - Control system volume
"Shutdown/restart" - System control
💬 AI Chat
Natural conversation with context memory
Task assistance and general queries
Conversation history persistence
🚀 Installation
Prerequisites
Python 3.7 or higher
Windows OS (for system control features)
Microphone for voice input
Spotify Premium account (for music features)
Setup Steps
Clone the repository

git clone https://github.com/yourusername/chaos-ai-assistant.git
cd chaos-ai-assistant
Install dependencies

pip install -r requirements.txt
Configure API Keys

cp config_template.py config.py
Edit config.py with your API credentials:

Google Gemini API key
Spotify Client ID and Secret
Run the assistant

python final.py
🔧 Configuration
Required API Keys
Google Gemini API
Visit Google AI Studio
Create a new API key
Add to config.py as apikey
Spotify API
Go to Spotify Developer Dashboard
Create a new app
Get Client ID and Client Secret
Add to config.py
Configuration Options
Edit config.py to customize:

TTS voice and speech rate
Audio timeout settings
File paths for logs and memory
📖 Usage
Text Mode
Welcome to CHAOS AI! Type 'exit' to quit or say 'exit' during audio input.
Type your command or say 'audio' for voice input:
> play despacito
Voice Mode
> audio
CHAOS: Listening for up to 5 seconds.
You said: play despacito
CHAOS: Playing Despacito by Luis Fonsi.
🎵 Spotify Setup
Install Spotify on your device
Log in to your Spotify Premium account
Keep Spotify running for music playback
First-time use will require authentication
📁 Project Structure
chaos-ai-assistant/
├── final.py                 # Main application
├── config_template.py       # Configuration template
├── requirements.txt         # Dependencies
├── README.md               # This file
├── .gitignore              # Git ignore rules
└── chat_memory.json        # Conversation history (auto-generated)
🛡️ Security Notes
Never commit config.py to version control
API keys are stored locally only
Conversation logs are stored locally
Use environment variables for production deployment
🚨 Troubleshooting
Common Issues
"config.py not found!"

Copy config_template.py to config.py
Add your API keys to the new file
Speech recognition not working

Check microphone permissions
Install pyaudio: pip install pyaudio
On Windows, you might need Microsoft Visual C++ 14.0
Spotify not playing

Ensure Spotify Premium account
Keep Spotify app running
Check device availability in Spotify
Voice not working

Install speech engines: pip install pyttsx3
Try different voice indices in config
🔄
