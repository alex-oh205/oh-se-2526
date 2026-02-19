# Import flask module
from flask2 import Flask

# Flask constructor takes the name of the current module
# (__name__) as argument
app = Flask(__name__)

# rout() function of Flask class is a decorator,
#  that tells the app which URL (which page) should call
#  the associated function.
# The name of the route must match the name of the function (except for the index page)

@app.route('/')    # index page route
def index():
    return "<h1>Landing Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# Main driving function
if __name__ == '__main__':

    # Run app through port 5000 on local dev. server
    app.run(debug=True)