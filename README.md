# 🌅 Muzamil's Morning Briefing AI

A personalized, voice-activated morning assistant designed for efficiency and inspiration. This system integrates your daily schedule, the latest news, and local Islamabad weather into a single poetic briefing.

## 🚀 Features
- **Open-Source Brain**: Powered by **Llama 3.3 (via Groq)** for ultra-fast, intelligent script generation.
- **Sufi-Inspired Greetings**: Starts your day with meaningful quotes (Rumi, Bulleh Shah, etc.).
- **Live Weather**: Real-time updates for **Islamabad** using the Open-Meteo API (no API key required).
- **Calendar Integration**: Fetches your actual schedule directly from **Google Calendar**.
- **Edge TTS**: Uses high-quality neural voices for a natural-sounding briefing.

## 🛠️ Project Structure
- `main.py`: The entry point that orchestrates the data fetching and speech.
- `brain_service.py`: Connects to Groq and manages the LLM logic.
- `weather_service.py`: Handles weather data retrieval.
- `calendar_service.py`: Manages Google Calendar API authentication and events.
- `news_service.py`: Web scrapes the latest headlines.

## 📦 Setup & Installation

### 1. Prerequisites
- Python 3.10+
- A [Groq API Key](https://console.groq.com/)
- Google Cloud Console `credentials.json` (with Calendar API enabled)

### 2. Local Setup
```bash
# Clone the repository
git clone [https://github.com/your-username/morning-briefing-ai.git](https://github.com/your-username/morning-briefing-ai.git)
cd morning-briefing-ai

# Install dependencies
pip install -r requirements.txt