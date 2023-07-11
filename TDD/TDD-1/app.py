from flask import Flask, jsonify
app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>')
def get_weather(city):
    if city in weather_data:
        return jsonify({
            'city': city,
            'temperature': weather_data[city]['temperature'],
            'weather': weather_data[city]['weather']
        })
    else:
        return jsonify({'error': 'City not found'}), 404


if __name__ == '__main__':
    app.run()
 