import requests
from flask import Flask, render_template

app = Flask(__name__)

API_URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 38.8951,
    "longitude": -77.0364,
    "hourly": "temperature_2m,apparent_temperature,precipitation_probability,precipitation",
    "daily": "temperature_2m_max,temperature_2m_min",
    "temperature_unit": "fahrenheit",
    "timezone": "America/Chicago"
}

# ... (previous imports and code) ...

# ... (previous imports and code) ...

@app.route('/')
def get_weather():
    response = requests.get(API_URL, params=PARAMS)
    data = response.json()

    hourly_data = data['hourly']
    time = hourly_data['time']
    temperature_2m = hourly_data['temperature_2m']
    apparent_temperature = hourly_data['apparent_temperature']
    precipitation_probability = hourly_data['precipitation_probability']
    precipitation = hourly_data['precipitation']
    
    daily_data = data['daily']

    return render_template(
        "weather.html",
        time=time,
        temperature_2m=temperature_2m,
        apparent_temperature=apparent_temperature,
        precipitation_probability=precipitation_probability,
        precipitation=precipitation,
        daily_data=daily_data
    )

if __name__ == '__main__':
    app.run(debug=True)
