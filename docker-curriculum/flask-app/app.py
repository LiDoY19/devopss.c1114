from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of images
images = [
    "https://c.tenor.com/0fI0vd8FEsoAAAAd/tenor.gif",
    "https://www.rockhamptonzoo.com.au/files/assets/rockyzoo/v/1/images-thumbs/meerkat-close-up-thumb-nail.png?dimension=pageimage&w=480",
    "https://c.tenor.com/0fI0vd8FEsoAAAAd/tenor.gif", 
    "https://c.tenor.com/4NLfMi7XI7kAAAAd/tenor.gif",
    "https://c.tenor.com/KMuLEm4XapgAAAAd/tenor.gif",
    "https://c.tenor.com/DXBMFHbQ0AAAAAAd/tenor.gif",
    "https://c.tenor.com/-VFGlrBlcSwAAAAd/tenor.gif",
    "https://c.tenor.com/WcoyIUKbg5oAAAAd/tenor.gif",
    "https://media1.tenor.com/m/306nYrZprbEAAAAd/timon-lion-king.gif",
    "https://media1.tenor.com/m/J4F181cEBV0AAAAd/the-lion-king-timon.gif",
    "https://media1.tenor.com/m/Kr7oesiWatIAAAAd/lion-king-oh-the-shame.gif", 
    "https://c.tenor.com/2GeIejx2hbYAAAAd/tenor.gif",
    "https://media1.tenor.com/m/v6w_poAU3LoAAAAd/achin-for-some-bacon-lion-king.gif",
    "https://media1.tenor.com/m/G34k5QDbCA0AAAAC/timon-and-pumbaa-cry.gif"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8888)))
