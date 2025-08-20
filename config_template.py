# config_template.py
# INSTRUCTIONS:
# 1. Copy this file and rename it to 'config.py'
# 2. Replace the placeholder values below with your actual API keys

# Google Gemini API Configuration
apikey = "your_google_gemini_api_key_here"

# Spotify API Configuration
SPOTIFY_CLIENT_ID = "your_spotify_client_id_here"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret_here"
SPOTIFY_REDIRECT_URI = "https://open.spotify.com/"
SPOTIFY_SCOPE = "user-library-read user-read-playback-state user-modify-playback-state"

# Text-to-Speech Configuration (Optional customization)
TTS_VOICE_INDEX = 1  # 0 for first voice, 1 for second voice, etc.
TTS_RATE = 150       # Speech rate (words per minute)
TTS_VOLUME = 1.0     # Volume level (0.0 to 1.0)

# Audio Input Configuration
AUDIO_TIMEOUT = 3    # Timeout for audio input in seconds
AUDIO_PHRASE_TIME_LIMIT = 5  # Maximum time for phrase recognition

# File Paths
CHAT_MEMORY_FILE = "chat_memory.json"
CONVERSATION_LOG_FILE = "conversation_log.txt"
