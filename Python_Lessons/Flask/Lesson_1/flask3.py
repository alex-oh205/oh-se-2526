# Import flask module
from flask import Flask, render_template

# Flask constructor takes the name of the current module
# (__name__) as argument
app = Flask(__name__)

# rout() function of Flask class is a decorator,
#  that tells the app which URL (which page) should call
#  the associated function.
# The name of the route must match the name of the function (except for the index page)

# Display a couple of sample blog posts
posts = [
    {
        'author': 'Gary Gygax',
        'title': 'AD & D Players Handbook',
        'content': 'Core rules and reference for the players',
        'date_posted': 'June 1978',
        'image': 'playersHandbook-small.jpg'
    },
    {
        'author': 'Frank Herbert',
        'title': 'Dune',
        'content': 'Book one in the Dune Chronicles',
        'date_posted': 'October 1, 1965',
        'image': 'dune-small.jpg'
    }
]

@app.route('/')    # index page route
def index2():
    return render_template('index2.html', posts=posts)

@app.route("/about2")
def about2():
    return render_template('about2.html', title='About')

# Main driving function
if __name__ == '__main__':

    # Run app through port 5000 on local dev. server
    app.run(debug=True)