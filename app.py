from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "75f2a1682081a98824409849dceb5ec8"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=75f2a1682081a98824409849dceb5ec8&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            error = data.get("message", "City not found")

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)