import os
from calendar_service import get_calendar_events
from news_service import get_local_headlines
from weather_service import get_today_weather
from brain_service import generate_morning_script
from voice_service import speak

def run_agent():
    print("--- Muzammil's AI Assistant is Starting ---")
    
    # Step 1: Get Calendar Data
    print("Agent: Checking your Google Calendar...")
    # This function should return a string of events
    events = get_calendar_events() 
    
    # Step 2: Get Weather Details
    print("Agent: Getting weather details...")
    weather = get_today_weather()
    
    # Step 3: Get Local News
    print("Agent: Scraping local news...")
    news = get_local_headlines()
    
    # Step 4: Generate the Script (The Brain)
    print("Agent: Thinking in Urdu...")
    final_script = generate_morning_script(events, news, weather)
    
    # Display the text in the terminal so you can read along
    print("\n--- TODAY'S BRIEFING ---")
    print(final_script)
    print("------------------------\n")
    
    # Step 4: Speak (The Voice)
    print("Agent: Speaking...")
    speak(final_script)
    
    print("--- Briefing Complete. Have a great day! ---")

if __name__ == "__main__":
    run_agent()