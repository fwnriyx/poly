from flask import Flask

def create_app ():
  web = Flask(__name__)
  web.config["SECRET_KEY"] = "cv%8!7nZrNrTdmPE" # randomly generated secret key

  # import blueprint
  from .app import app
  web.register_blueprint(app, url_prefix="/")

  return web