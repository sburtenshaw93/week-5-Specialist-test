##### INTRODUCTION #####
# In Python, we use the 'from PACKAGE import ITEMS' syntax 
# In this app, we are importing the main Flask class, which will allow
# us to create our app 
# We are also importing 'request', 'render_template', and `send_from_directory` 
# which are utilities that allow us to interact with HTTP(s) requests, HTML 
# templates, and statis files respectively
from flask import Flask, request, render_template, send_from_directory


##### APP SETUP #####
# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
# This line sets up our whole app for us, similar to an express app in node. 
app = Flask(__name__, static_url_path='/images')


##### ROUTES #####
# In the Flask documentation, it states: 
# "We then use the route() decorator to tell Flask what URL should trigger our function.
# The function returns the message we want to display in the user’s browser. The default 
# content type is HTML, so HTML in the string will be rendered by the browser."
# Basically, this means we can easily set up routes and what they'll render using this 
# pattern: 
    # @app.route('/path')
    # def path_fn(): 
    #     return "<html>"

# Here we can see that pattern in action 
# home.html is in the `templates` directory
@app.route('/')
def start_here():
    """Home page."""

    return render_template('home.html')


##### STEP 1 #####
# Ensure that you are in your virtual environment - you'll be able to tell if in your
# terminal it says `(venv)` at the beginning of the line (check the instructions in Frodo
# if you're wondering how to activate it)

# Run the command `pip install Flask`
# pip is another tool you gained when you downloaded Python 

# When the install is complete, run `python server.py`
# Open up the browser to localhost 5000 and you should see the home page!

# You should also be able to click the link to go to the next route, let's fix it so that 
# we can see the dino creation form!

# When you save files, you may have to refresh your browser to see your changes.

# You can stop the server by pressing `ctrl + c`.


##### STEP 2 #####
# Using the `render_template` function that we imported from flask, 
# change the `return` of the `get_info` function below so that it 
# returns the `form.html` template

# Hint: take a look at the `start_here` function above 

@app.route('/form')
def get_info():
    # The next line is an explanation of what this function does.
    """Display dino creation form."""

    return render_template('form.html')


##### WITHOUT RENDER_TEMPLATE #####
# We do not have to use the `render_template` function with Flask. In fact, we can 
# write HTML directly in a string and return that from our functions! We will practice 
# that in our last function below. 


##### F-STRINGS #####
# In Python, we can use f-strings to insert data directly into strings without 
# using concatenation (think: string interpolation, template strings, string literals).
# To create an f-string, just type an "f" followed by whatever quotes you're using.
# Example: 
    # color = 'red'
    # print(f"The best color is {color}.")

# This is similar to using backticks, dollar signs, and curly braces in JavaScript. 
# JS Example: 
    # let color = 'red'
    # console.log(`The best color is ${color}.`)


##### TRIPLE QUOTES ##### 
# In Step 3, you'll want to use triple quotes to create your f-string since in Python 
# that is how we can write multi-line strings. 
# Example: 
    # f"""
    # Wow, look at 
    # this! It's a 
    # multi-line string. 
    # """


##### REQUEST #####
# Flask provides us access to `request` which is an object that contains information
# about HTTP requests. From this object, we can actually get information that our users 
# sent on the form they filled out. 

# For example, if on the form, one of the inputs had the value "info" saved to a `name` 
# attribute, we could access that information like so: 
    # HTML:
    # <input type="text" name="info"/>
    # Flask:
    # info = request.args.get("info")


##### STEP 3 #####
# This last route is a page that will display the information that you provided 
# about your dinosaur. 

# Open up `form.html` and find the `name` attributes for each of the inputs. 
# Note: Since there are radio buttons for the pictures, they all share a `name`.

# In the `display_dino` function, above the return, create three variables - 
# `image`, `dino_name`, and `age`.
# They should store the data that you get from `request.args` for the `name` attributes 
# you found using the syntax from the example in the comments above.

# The outline of the HTML has been given to you. Now you get to create whatever 
# page you'd like! Just be sure to use the dino's name, image, and age somewhere 
# on your page. Remember, we are returning an f-string, so we can insert variables 
# using curly braces. 

# If you're having trouble with the image, take a look at `form.html` and the `static_dir`
# function near the bottom of this file. 

# Note that we are importing the `main.css` file.

# You can also look at the solution file if you're not sure how to complete this step. 

@app.route('/dino')
def display_dino():
    """Display the dino."""
    image = request.args.get("dino-pic")
    dino_name = request.args.get("dino-name")
    age = request.args.get("age")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Your Title Here</title>
        <link rel="stylesheet" href="/static/main.css">
      </head>
      <body>
        <main>
            img src="/static/images/dinoThree.png" alt="dinosaur"/>
            <h1>This is {dino_name}. He's {age} years old.</h1>
            <a href="/form">Create another dinosaur.</a>
        </main>
      </body>
    </html>
    """

##### WHAT'S THIS DOING #####
# This route allows us to serve assets from our "static" folder 
# this is where all of our images and CSS are stored, so any time 
# we want to use something from that folder, we use the path from 
# the root of the project instead of the relative path.
@app.route('/static/<path:path>')
def static_dir(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

# ALL DINOSAUR IMAGES ARE FROM Darius Dan on Flaticon