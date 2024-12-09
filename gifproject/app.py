import os
from flask import Flask, render_template
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'mydatabase')

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT url FROM gifs ORDER BY RAND() LIMIT 1;")
        result = cursor.fetchone()
    connection.close()
    
    gif_url = result['url'] if result else None
    return render_template('index.html', gif_url=gif_url)

if __name__ == '__main__':
    # Use the environment variables for host/port if available
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(host=host, port=port)