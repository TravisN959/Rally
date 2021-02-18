from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import requests
import json
import accounts

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        try:
            
            return 'hi'
        except:
            return 'There was an error searching your task'

    else:#page refreshed/ reloaded so will output the template.
        return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
@app.route('/signup.html', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repeatPass = request.form['repeatPassword']
        if(password != repeatPass): #check for repeat password
            try:
                return render_template('signup.html', ERROR=True, ERROR_MSG="Passwords must be the same")
            except: return "Error in repeat password"
        elif(accounts.checkDuplicateUsername(username)): #check for username alreadu in db
            try:
                return render_template('signup.html', ERROR=True, ERROR_MSG="Duplicate: Choose a new username")
            except: return "Error in duplicate username"
        else:#add account to db
            accounts.addAccount(username, password)
            try:
                
                return 'added'
            except:
                return 'There was an error searching your task'

    else:#page refreshed/ reloaded so will output the template.
        return render_template('signup.html', ERROR=False, ERROR_MSG="No Error")

if __name__ == "__main__":
    app.run(debug=True)