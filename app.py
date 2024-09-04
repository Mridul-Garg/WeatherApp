from flask import Flask, render_template, request
import requests
from config import api_key

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        print(weather_data)
        print(weather_data)
        if weather_data.get('cod') != 200:
            return render_template('index.html', error="City not found.")
        weather = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
        return render_template('index.html', weather=weather)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


