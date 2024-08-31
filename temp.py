from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

import os

app = Flask(__name__, template_folder='/Users/anav_sobti/Desktop/AIRTEL Automation/users_data.csv')
CORS(app)

# Define the path to your CSV file
csv_file_path = '/Users/anav_sobti/Desktop/AIRTEL Automation/users_data.csv'

# Initialize the CSV file with headers if it does not exist
if not os.path.exists(csv_file_path):
    df = pd.DataFrame(columns=['Name', 'Email', 'Age', 'GST Number'])
    df.to_csv(csv_file_path, index=False)

@app.route('/add-user', methods=['POST'])
def add_user():
    try:
        # Get the user data from the request
        user_data = request.json

        # Extract the fields from the JSON data
        name = user_data.get('name')
        email = user_data.get('email')
        age = user_data.get('age')
        gst_number = user_data.get('gst_number')

        # Create a new DataFrame for the new user data
        new_data = pd.DataFrame([{
            'Name': name,
            'Email': email,
            'Age': age,
            'GST Number': gst_number
        }])

        # Append the new data to the existing CSV file
        new_data.to_csv(csv_file_path, mode='a', header=False, index=False)

        return jsonify({'message': 'User data added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port = 5001)
    
