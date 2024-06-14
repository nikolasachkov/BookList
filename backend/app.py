from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)
CORS(app)

# Database Configuration
db_config = {
    'user': os.getenv('DB_USER', 'maxscale_user'),
    'password': os.getenv('DB_PASSWORD', '12345678'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '4006'),
    'database': os.getenv('DB_NAME', 'booklist')
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'name' not in data or 'author' not in data or 'genre' not in data:
        return jsonify({'message': 'Missing data'}), 400

    name = data['name']
    author = data['author']
    genre = data['genre']

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO books (name, author, genre) VALUES (%s, %s, %s)', (name, author, genre))
            conn.commit()
            return jsonify({'message': 'Book added successfully!'}), 201
        except mysql.connector.Error as e:
            print(f"Failed to insert book: {e}")
            return jsonify({'message': 'Failed to add book'}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'message': 'Connection to database failed'}), 500

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the BookList API!'}), 200

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
