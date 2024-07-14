from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#Login Password for OpenWeatherAPI is Koodal@7598

@app.route('/')
def index():
    return render_template('openweatherapi.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    #API KEY Generated at OpenWeather Website
    api_key = '189d88fcd75775ce99b95b872c4752c7'  

    if not city:
        return render_template('openweatherapi.html', error='Please enter a city name.')

    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        response.raise_for_status()
        weather_data = response.json()

        if weather_data['cod'] == '404':
            return render_template('openweatherapi.html', error='City not found. Please check the city name.')

        weather_description = weather_data['weather'][0]['description']
        temperature = round(weather_data['main']['temp'] - 273.15, 2)  # Convert to Celsius

        return render_template('openweatherapi.html', city=city, description=weather_description, temperature=temperature)
    except requests.exceptions.RequestException as e:
        return render_template('openweatherapi.html', error=f'Error fetching weather data: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
