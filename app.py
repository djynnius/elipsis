#import system modules
import gc #garbage collector
from flask import Flask, render_template

#import controllers
from controllers import admin

#import models
from models import users

db = users.db
User = users.User

#instantiate Flask
app = Flask(__name__)

#register controllers
app.register_blueprint(admin.admin_controller)

#routes
@app.route("/")
def index():
    foo = User()
    return render_template("landing.html")

if __name__ == "__main__":
    app.run(port=9999)

gc.collect() #garbage collection to ensure no memory issues
