from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import UserMixin

app = Blueprint('app', __name__)

def upload_data(filepath: str, data: any):
  with open(filepath, "w") as f:
    f.write(f"{data}")
    return
  

class User(UserMixin):
    def __init__(self, username):
        self.username = username
    
    def get_id(self):
        return self.username
    
#Only will have 1 user connected to a band at a time

userInfo = {
   "username": "test",
   "password": "123"
}

@app.route("/")
def index():
    return render_template('home.html', methods=["GET"])

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if user == userInfo["username"]:
            #Since this project doesn't require a database,
            #we will just be referring to the test user info.
            #In a real situation, we would use an sql database in order to 
            #store users and passwords, and connecting to the input to check.
            if password == userInfo["password"]:
                userObj = User(username = userInfo["username"])
                return render_template('home.html', methods=["GET"])
            else:
                error = "Invalid username or password"
        return render_template('login.html', error = error)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template('signup.html', methods=["GET"])

@app.route("/viewdata", methods=["GET", "POST"])
def viewdata():
    return render_template('data.html', methods=["GET"])

@app.route('/update_thingspeak', methods=['POST'])
def update_thingspeak():
    data = request.get_json()
    heart_rate = data.get('heart_rate')
    steps = data.get('steps')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    dist_travelled = data.get('dist_travelled')

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")