from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import mysql.connector
from datetime import date

app = Flask(__name__)
CORS(app)

# Define MySQL database connection parameters
db_config = {
    'user': 'cn_user',
    'password': 'cn_password',
    'host': 'cn-db',
    'port': 3306,
    'database': 'diary',
}

# Create a MySQL database connection
db_connection = mysql.connector.connect(**db_config)

# Create a cursor for executing SQL queries
db_cursor = db_connection.cursor()

@app.route('/contents', methods=['GET'])
@cross_origin()
def get_contents():
    db_cursor.execute('SELECT * FROM content')
    contents = db_cursor.fetchall()

    # Convert results to JSON format
    content_list = []
    for content in contents:
        content_dict = {
            'id': content[0],
            'contents': content[1],
            'date': content[2].strftime('%Y-%m-%d'),
        }
        content_list.append(content_dict)

    return jsonify(content_list)

@app.route('/contents', methods=['POST'])
@cross_origin()
def create_content():
    data = request.get_json()
    contents = data.get('contents')

    if not contents:
        return jsonify({'error': 'Content is required'}), 400

    # Insert new content into the database
    insert_query = 'INSERT INTO content (contents, date) VALUES (%s, %s)'
    db_cursor.execute(insert_query, (contents, date.today()))
    db_connection.commit()

    return jsonify({'message': 'Content created successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
