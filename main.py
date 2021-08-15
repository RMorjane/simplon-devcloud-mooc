from flask import Flask, request, render_template, jsonify
from db_mooc import DBMooc, Role
import logging
import json

logging.basicConfig(filename='logs.log',level=logging.DEBUG)

db = DBMooc()
db.connect()
db.read_roles()

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    menu = request.args.get("menu")
    print(menu)
    return render_template("index.html")

@app.route('/<item>',methods=['GET'])
def menu(item):
    return render_template(item + ".html")

@app.route('/user/signup',methods=['POST'])
def signup():
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    print("email : %s\nusername : %s\npassword 1 : %s\npassword 2 : %s" %(email,username,password1,password2))
    return "received"

if __name__ == "__main__":
    #app.run(host="0.0.0.0",port=3000, debug=True)
    
    role = Role()
    role.set_roleID(1)
    role.read_name(db)
    print(role)