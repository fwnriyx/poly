from flask import Blueprint, Flask, render_template, request, redirect, url_for
from flask_login import UserMixin
import random
import json
import os
import requests # for thingspeak
import time

app = Blueprint('app', __name__)

# upload data to file
def upload_data(filepath: str, data: any):
  with open(filepath, "w") as f:
    f.write(f"{data}")


  return
class User(UserMixin):
  def __init__(self, username):
    self.username = username

  def get_id(self):
    return self.username



# user login credentials (only have 1 user since each rpi will be connected to only 1 door lock)
userCred = {
  "username": "test",
  "password": "test123"
}

# for thingspeak, "1" = generate OTP, "2" = password mode
doorLockMode = {
  "otp": 1,
  "password": 2
}

# telegram notif
TOKEN = "6044657815:AAGGrGvHPIDhKiayFyuNxmEUrjnVGTfGz3Y"
chat_id = 837915524
message = ""


@app.route("/")
def index():
  return render_template('login.html', methods=["GET"])


@app.route("/login", methods=["GET", "POST"])
def login():
  error = None
  if request.method == "POST":
    inputUsername = request.form["username"]
    inputPassword = request.form["password"]
    # check if username matches
    if userCred["username"] == inputUsername:
      # check if password matches
      if userCred["password"] == inputPassword:
        userObj = User(username=userCred["username"])
        return redirect(url_for("app.validUser", loggedInStatus="false"))
      else:
        # incorrect password
        error = "Incorrect username or password"
        # send telegram msg to "home owner"
        message = "A user has attempted to login to the webpage, but failed"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

        # "0" for unauthorized
        resp = requests.get("https://api.thingspeak.com/update?api_key=OLFWBE5G3976RQ3H&field1=%s" %0)
        time.sleep(20)
        return redirect(url_for("app.unauthorized"))
      
    else:
      # incorrect username
      error = "Incorrect username or password"
      # send telegram msg to "home owner"
      message = "A user has attempted to login to the webpage, but failed"
      url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
      requests.get(url).json()

      # "0" for unauthorized
      resp = requests.get("https://api.thingspeak.com/update?api_key=OLFWBE5G3976RQ3H&field1=%s" %0)
      time.sleep(20)
      return redirect(url_for("app.unauthorized"))
    
  return render_template("login.html", error = error)


@app.route("/authorized/<loggedInStatus>", methods=["GET", "POST"])
def validUser(loggedInStatus):
  if request.method == "POST":
      # for thingspeak, "1" = generate OTP, "2" = password mode
      try:
        if "generate-otp" in request.form:
          # generate OTP
          return redirect(url_for("app.generate_otp"))
        
        elif "passcode-mode" in request.form:
          return redirect(url_for("app.password"))
        
        else:
          pass

      except:
        pass
  
  # prevent continuous telegram msg from redirecting from password/otp webpage
  if loggedInStatus == "true":
    return render_template("authorized.html")
  
  else:
    # send telegram msg to "home owner"
    message = "A user has logged into the webpage"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
    
    # "1" for authorized
    resp = requests.get("https://api.thingspeak.com/update?api_key=OLFWBE5G3976RQ3H&field1=%s" %1)
    time.sleep(20)
    return render_template("authorized.html")


@app.route("/unauthorized", methods=["GET", "POST"])
def unauthorized():
  if "home" in request.form:
    return redirect(url_for("app.login"))
  else:
    pass
  return render_template("unauthorized.html")


@app.route("/generate_otp", methods=["GET", "POST"])
def generate_otp():
  error = ""

  # generate OTP
  otp = random.randint(100000, 999999)
  upload_data("./server/database/otp.txt", int(otp))

  if request.method == "POST":
    try:
      if "back" in request.form:
        return redirect(url_for("app.validUser", loggedInStatus="true"))
      else:
        pass

    except:
      pass
  
  # send telegram msg to "home owner"
  message = "A one-time password has been generated: %s" %otp
  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url).json()

  # insert send OTP and door lock mode to thingspeak here
  resp = requests.get("https://api.thingspeak.com/update?api_key=OLFWBE5G3976RQ3H&field3=%s&field4=%s" %(otp, doorLockMode["otp"]))
  time.sleep(20)
  return render_template("generate-otp.html", otp=otp, error=error)


@app.route("/password", methods=["GET", "POST"])
def password():
  if request.method == "POST":
    try:
      if "back" in request.form:
        return redirect(url_for("app.validUser", loggedInStatus="true"))

      else:
        pass

    except:
      pass

  # send telegram msg to "home owner"
  message = "Door is set to 'password mode', please enter the password into keypad to unlock the door"
  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
  requests.get(url).json()

  # insert set door lock to password mode here
  resp = requests.get("https://api.thingspeak.com/update?api_key=OLFWBE5G3976RQ3H&field4=%s" %doorLockMode["password"])
  time.sleep(20)
  return render_template("password.html")

