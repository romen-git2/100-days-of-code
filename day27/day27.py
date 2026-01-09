import requests
from dataclasses import dataclass
from typing import Optional

@dataclass
class UserLocation:
    name: str
    city: str
    lat: float
    lng: float

# get user
def get_user_location(user_id: int) -> Optional[UserLocation]:
    """Fetches user profile and extracts geo coordinates"""
    print(f"Fetching profile for User ID: {user_id}...")
    
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # navigate nested JSON to find coordinates
        user_loc = UserLocation(
            name=data['name'],
            city=data['address']['city'],
            lat=float(data['address']['geo']['lat']),
            lng=float(data['address']['geo']['lng'])
        )
        print(f"Found: {user_loc.name} living in {user_loc.city}({user_loc.lat}, {user_loc.lng})")
        return user_loc
        
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None

# get weather
def get_weather_at_coords(lat: float, lng: float) -> str:
    """Uses coordinates to fetch real-time weather data"""
    print(f"Checking weather at {lat}, {lng}...")
    
    # Open-Meteo API
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lng,
        "current_weather": "true"
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # extract specific data points
        current = data['current_weather']
        temp = current['temperature']
        wind = current['windspeed']
        
        return f"{temp}°C with wind speeds of {wind} km/h"
        
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return "Unknown Weather"

def run_agent_chain(target_user_id):
    print(f"Starting Context Chain(Target: User {target_user_id})")
    
    # chain link 1 - get data
    user = get_user_location(target_user_id)
    
    if not user:
        print("Chain broke at Step 1.")
        return

    # chain link 2 - enrich data
    weather_report = get_weather_at_coords(user.lat, user.lng)
    
    print(f"User: {user.name}")
    print(f"Location: {user.city}")
    print(f"Status: Currently experiencing {weather_report}")

if __name__ == "__main__":
    run_agent_chain(5)