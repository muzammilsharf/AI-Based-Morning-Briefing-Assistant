import requests

def get_today_weather(city="Islamabad"):
    # Coordinates for Islamabad
    lat, lon = 33.6844, 73.0479
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    
    try:
        response = requests.get(url).json()
        current = response['current_weather']
        daily = response['daily']
        
        weather_report = (
            f"The current temperature in {city} is {current['temperature']}°C. "
        )
        return weather_report
    except Exception as e:
        return "Temperature not available right now."
    