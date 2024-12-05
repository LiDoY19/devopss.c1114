from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Random Dog Image App</h1><p>Visit /dog for a random dog image!</p>"

@app.route("/dog")
def dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        # Corrected to use .json() instead of .jason()
        dog_data = response.json()
        dog_image_url = dog_data.get("message", "")
        return render_template("dog.html", image_url=dog_image_url)
    else:
        return "<h1>Failed to fetch the dog image. Please try again later.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)