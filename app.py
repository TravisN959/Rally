from flask import Flask, render_template, url_for, request, redirect, session
from datetime import datetime
import requests
import json
import accounts

app = Flask(__name__)
app.secret_key = "rally"

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        try:
            
            return 'hi'
        except:
            return 'There was an error searching your task'

    else:#page refreshed/ reloaded so will output the template.
        
        return render_template('index.html', signedIn= isloggedIn())

@app.route('/signup', methods=['POST', 'GET'])
@app.route('/signup.html', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        repeatPass = request.form['repeatPassword']
        if(password != repeatPass): #check for repeat password
            try:
                return render_template('signup.html', ERROR=True, ERROR_MSG="Passwords must be the same", signedIn= isloggedIn())
            except: return "Error in repeat password"
        elif(accounts.checkDuplicateUsername(username)): #check for username alreadu in db
            try:
                return render_template('signup.html', ERROR=True, ERROR_MSG="Duplicate: Choose a new username", signedIn= isloggedIn())
            except: return "Error in duplicate username"
        else:#add account to db
            accounts.addAccount(username, password)
            try:
                
                return signupSuccess()
            except:
                return 'There was an error searching your task'

    else:#page refreshed/ reloaded so will output the template.
        return render_template('signup.html', ERROR=False, ERROR_MSG="No Error", signedIn= isloggedIn())

@app.route('/signin', methods=['POST', 'GET'])
@app.route('/signin.html', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        if(not accounts.validateLogin(username, password)): #check for correctinfo
            try:
                return render_template('signin.html', ERROR=True, ERROR_MSG="Password/Username Combo Error: Try Again", signedIn= isloggedIn())
            except: return "Error in sigin"
        session["user"] = username #creates session for user
        return redirect(url_for("mainPage"))
    else:#page refreshed/ reloaded so will output the template.
        return render_template('signin.html', ERROR=False, ERROR_MSG="No Error", signedIn= isloggedIn())

@app.route('/signupSuccess')
def signupSuccess():
    return render_template('signupSucccess.html', signedIn= isloggedIn())

@app.route('/mainPage', methods=['POST', 'GET'])
@app.route('/mainPage.html', methods=['POST', 'GET'])
def mainPage():
    if "user" in session:#checks to see if logged in
        if request.method == 'POST':
            return session["user"]
            # username = request.form['username']
            # username = username.lower()
            # password = request.form['password']
            # if(not accounts.validateLogin(username, password)): #check for correctinfo
            #     try:
            #         return render_template('signin.html', ERROR=True, ERROR_MSG="Password/Username Combo Error: Try Again")
            #     except: return "Error in sigin"
            # session["user"] = username
            # return render_template('mainPage.html')
        else:#page refreshed/ reloaded so will output the template.
            return session["user"]#render_template('mainPage.html')
    else:
        return render_template('signin.html', signedIn= isloggedIn())

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("signin"))


def isloggedIn():
    if "user" in session:
        return True
    else:
        return False
if __name__ == "__main__":
    app.run(debug=True)