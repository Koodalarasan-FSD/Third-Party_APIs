from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Login Password for OpenWeatherAPI is Koodal@7598

@app.route('/')
def index():
    return render_template('openweatherapicurrentlocation.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    latitude=request.form.get('latitude')
    longitude=request.form.get('longitude')

    api_key = '189d88fcd75775ce99b95b872c4752c7'  # Replace with your OpenWeatherMap API key

    if not latitude or not longitude:
        return render_template('openweatherapicurrentlocation.html', error='Please enable geolocation and try again.')
    
    try:
        # Get the user's current location using the HTML5 Geolocation API
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}')
        response.raise_for_status()
        weather_data=response.json()

        if weather_data['cod'] == '404':
            return render_template('openweatherapicurrentlocation.html', error='Weather data not found for the current location.')
        
        weather_description = weather_data['weather'][0]['description']
        temperature = round(weather_data['main']['temp'] - 273.15, 2)  # Convert to Celsius

        return jsonify({
            'city': weather_data['name'],
            'description': weather_description,
            'temperature': temperature
        })
    
    
    except requests.exceptions.RequestException as e:
        return render_template('openweatherapicurrentlocation.html', error=f'Error fetching location data: {str(e)}')
    
    
   

        
        

        
    

if __name__ == '__main__':
    app.run(debug=True)
