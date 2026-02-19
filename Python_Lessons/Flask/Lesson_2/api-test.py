# Filename:  app-test.py
# Flask app for Flask + Firebase 
# Coded By:  

# Flask app to test sending user's Firebase information to Flask & writing sample data usign Pyrebase4

from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime
import pyrebase

app = Flask(__name__)

config = {}
key = 0 # If recording data over time, keys should be seconds or milliseconds from 0.

# Notes:
# 1.  The  @app.route parameter (in parantheses) should match the name of the page to 
#     which it routes, without the ".html"
#     Ex.  If routing to signIn.html:   @app.route("/signIn")  -- You need to add the 
#     forward slash before the parameter
#     The only exception is the @app.route for the index page:  @app.route("/")
# 2.  When linking to index.html from other html pages when using Flask, 
#     use {{url_for('index')}}.  The name of the python function (__name__) is used as 
#     the endpoint, unless you specify the endpoint argument explicitly.
#     Ex.  {{url_for('index')}} will redirect the user to index.html because 
#     "index" is the name of the defined route function

@app.route('/')    # index page route
def index():
    return render_template('index.html', title='index')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/signIn')
def signIn():
    return render_template('signIn.html', title='Sign In')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

# Route to test Pyrebase setup and transfer Arduino data to Firebase
@app.route('/test', methods=['GET', 'POST'])
def test():
    global config, userID, db, timeStamp, key, idToken

    # POST request (FB configuration sent from login.js, request.method defaults to GET)
    if request.method == 'POST':

        # Each data set will be stored under its own child node identified by a timestamp
        # Get time stamp to be used as firebase node
        timeStamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Receive Firebase configuration credentials, pop uid and assign to userID
        config = request.get_json()
        userID = config.pop('userID')
        idToken = config.pop('idToken')
        
        # Output to a console (or file) is normally buffered (stored) until it is
        # forced out by the printing of a newline. Flush will force the information
        # in the buffer to be printed immediately.

        print('User ID: ' + userID, flush=True)     # Debug only
        print(config, flush=True)                   # Debug only
        print('ID Token: ' + idToken, flush=True)   # Debug only

        # Initialize firebase connection
        firebase = pyrebase.initialize_app(config)

        # Create a database object ("db" represents the root node in the database)
        db = firebase.database()

        # Write sample data to FB to test connection
        db.child('users/' + userID + '/data/' + timeStamp).update({'testKey': 'testValue'}, idToken)

        return 'Success', 200
    
    # If a GET request is made, check to see if the FB configuration has been provided. If not,
    # do nothing. If so, update the Firebase with the sensor data.
    else:
        if not config:
            print("FB config is empty")
        else:
            # Take parameters from Arduino request & assign value to variable "value"

            # print(config)
            value = request.args.get('distance')

            print('Distance: ' + value, flush=True)
            
            # Write Arduino data to Firebase
            db.child('users/' + userID + '/data/' + timeStamp).update({key:value}, idToken)

            # Increment key
            key += 1
        
        return 'Success', 200

# Run server on local IP address on port 5000
    # If you see the error: "The requested address is not valid in its context" it means
    # IP address specified for the host is incorrect.
if __name__ == '__main__':
    app.run(debug=False, host='192.168.0.11', port=5000)