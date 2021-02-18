from flask import Flask, render_template, url_for, request, redirect, session
from datetime import datetime
import requests
import json
import accounts
import accountInfo
import topics
import rallydb
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

        fname = request.form['fname']
        lname = request.form['lname']
        
        phone = request.form['phone']
        email = request.form['email']
        
        address= {}
        address["street"] = request.form["street"]
        address["state"] = request.form["state"]
        address["city"] = request.form["city"]
        address["zip"] = request.form["zip"]
        #get info for default topics
        topicso = []
        
        for top in topics.getTopics():
            idnum = top["idNum"]
            topicVal = 'topic' + str(idnum)
            topic = request.form.get(topicVal)
            if topic is not None:
                topicso.append(idnum)

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
            accountInfo.setupAccount(username, phone, email, topicso, fname, lname, address)
            try:
                
                return signupSuccess()
            except:
                return 'There was an error searching your task'

    else:#page refreshed/ reloaded so will output the template.
        return render_template('signup.html', ERROR=False, ERROR_MSG="No Error", signedIn= isloggedIn(), topicsInput= topics.getTopics())

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
        return render_template('mainPage.html',signedIn= isloggedIn(), rallys= rallydb.getRallys())
    else:
        return render_template('signin.html', signedIn= isloggedIn())

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("signin"))

@app.route('/rallySuccess')
def rallySuccess():
    return render_template('rallySuccess.html', signedIn= isloggedIn())

@app.route('/rally', methods=['POST', 'GET'])
def rally():
    if "user" in session:#checks to see if logged in
        
        if request.method == 'POST':
            name = request.form["name"]
            description = request.form["description"]
            address = {}
            address["street"] = request.form["street"]
            address["city"] = request.form["city"]
            address["state"] = request.form["state"]
            address["zip"] = request.form["zip"]
            imageAddress = request.form["imageAddress"]
            link = request.form["link"]
            eventDate = request.form["eventDate"]
            topic = request.form["topics"]
            creator = session["user"]

            idIn = rallydb.getRallyCount()
            #add rally to list in topics
            # topics.addRally(topic, idIn)
            #add rally to rally db
            rallydb.setupRally(idIn, name, description, address, imageAddress, link, eventDate, topic, creator)
            return redirect(url_for("rallySuccess"))
        else:
            return render_template('rally.html', signedIn= isloggedIn(), topics= topics.getTopics())
    else:
        return render_template('signin.html', signedIn= isloggedIn())

@app.route('/topicCreate', methods=['POST', 'GET'])
def topicCreate():
    if "user" in session:#checks to see if logged in
        if request.method == 'POST':
            name = request.form["name"]
            description = request.form["description"]
            idNum = topics.getTopicsCount() + 1
            rallys = []
            topics.setupTopic(idNum, name, description, rallys)
            return 'created'
        else:
            return render_template('topicCreate.html', signedIn= isloggedIn())
    else:
        return render_template('signin.html', signedIn= isloggedIn())


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if "user" in session:#checks to see if logged in
        if request.method == 'POST':
           
            return render_template('settings.html', signedIn= isloggedIn())
        else:
            return render_template('settings.html', signedIn= isloggedIn())
    else:
        return render_template('signin.html', signedIn= isloggedIn())

def isloggedIn():
    if "user" in session:
        return True
    else:
        return False
if __name__ == "__main__":
    app.run(debug=True)