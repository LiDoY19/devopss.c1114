import time
import mysql.connector
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load secrets
def get_secrets():
    secrets = {}
    with open('/run/secrets/db_secrets', 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            secrets[key] = value
    return secrets

secrets = get_secrets()

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://root:{secrets['MYSQL_ROOT_PASSWORD']}@db/{secrets['MYSQL_DATABASE']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Retry database connection
def wait_for_db():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password=secrets['MYSQL_ROOT_PASSWORD']
            )
            conn.close()
            break
        except mysql.connector.Error:
            print("Waiting for database...")
            time.sleep(5)

wait_for_db()

# Define the Image model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)

@app.route("/")
def index():
    image = Image.query.order_by(db.func.random()).first()
    return render_template("index.html", url=image.url if image else None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)