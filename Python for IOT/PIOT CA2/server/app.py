from flask import Flask, Blueprint, render_template, request, jsonify, url_for, redirect
import requests
from datetime import datetime

app = Flask(__name__)

user_info = {
   "username": "test",
   "password": "123"
}

class User:
    def __init__(self, username):
        self.username = username
    
    def get_id(self):
        return self.username

def fetch_data(channel_id, api_key, field_num):
    url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&field{field_num}=true'

    # Fetch data
    response = requests.get(url)
    data = response.json()
    print(data)
    assert response.status_code == 200

    # Extract relevant information from the response and convert to integers
    field_data = []
    for entry in data['feeds']:
        if entry[f'field{field_num}'] is not None:
            try:
                value = float(entry[f'field{field_num}'])
                field_data.append(value)
            except ValueError:
                # Handle the case where the value is not convertible to an integer
                pass

    return field_data


@app.route("/", methods=["GET"])
def index_page():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        # print(user, password)
        # print(user_info["username"], user_info["password"])
        if user == user_info["username"]:
            print("hello")
            if password == user_info["password"]:
                print("hellllllooooooo")
                # user_obj = User(username=user_info["username"])
                return redirect(url_for("viewdata"))
            else:
                error = "Invalid username or password"
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)


@app.route("/viewdata", methods=["GET"])
def viewdata():
    channel_id = 2406556
    api_key = 'FPC7UEB6NHIZXH0O'

    # Fetch and clean data for each field
    field1_data = fetch_data(channel_id, api_key, 1)
    field2_data = fetch_data(channel_id, api_key, 2)
    field3_data = fetch_data(channel_id, api_key, 3)
    field4_data = fetch_data(channel_id, api_key, 4)
    field5_data = fetch_data(channel_id, api_key, 5)

    return render_template('data.html',
                           title='View Data',
                           field1_data=field1_data,
                           field2_data=field2_data,
                           field3_data=field3_data,
                           field4_data=field4_data,
                           field5_data=field5_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")