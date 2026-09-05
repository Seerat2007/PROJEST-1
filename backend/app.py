from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Weather backend is running!"


@app.route("/api/weather")
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    try:
        # 1. Find the city coordinates
        location_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            }
        )

        location_data = location_response.json()
        results = location_data.get("results", [])

        if not results:
            return jsonify({"error": "City not found"}), 404

        location = results[0]

        # 2. Get weather using latitude and longitude
        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                "timezone": "auto"
            }
        )

        weather_data = weather_response.json()
        current = weather_data["current"]

        # Convert weather codes into readable descriptions
        weather_descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Foggy",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            61: "Light rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Light snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Rain showers",
            81: "Rain showers",
            82: "Heavy rain showers",
            95: "Thunderstorm"
        }

        # 3. Send a clean response to the frontend
        return jsonify({
            "city": location["name"],
            "country": location.get("country"),
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "windSpeed": current["wind_speed_10m"],
            "weatherCode": current["weather_code"],
            "description": weather_descriptions.get(
                current["weather_code"],
                "Unknown weather"
            )
        })

    except Exception as error:
        print("Error:", error)
        return jsonify({"error": "Unable to fetch weather data"}), 500


if __name__ == "__main__":
    app.run(debug=True)