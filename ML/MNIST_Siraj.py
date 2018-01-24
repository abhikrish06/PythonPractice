# https://www.youtube.com/watch?v=f6Bf3gl4hWY

# import the flask library
from flask import Flask

# Initialize the app from the flask
app = Flask(__name__)

# Define the route to hello world function
@app.route('/')
def hello_world():
    return 'Hello World!'

# Run the app on http://localhost:8085
app.run(debug=True,port=8085)
