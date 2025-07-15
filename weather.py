import requests

DEFAULT_LAT = 37.9838
DEFAULT_LON = 23.7275

def get_current_weather(lat: float = DEFAULT_LAT, lon: float = DEFAULT_LON) -> dict:
    """
    Fetch current weather from Open-Meteo API.
    Returns a dict with temperature (°C), weather code, and time.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        # Optionally, add hourly/daily fields later
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    cw = data.get("current_weather", {})
    return {
        "temperature": cw.get("temperature"),
        "windspeed": cw.get("windspeed"),
        "weathercode": cw.get("weathercode"),
        "time": cw.get("time"),
    }
