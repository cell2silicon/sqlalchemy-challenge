from flask import Flask, jsonify

# Dictionary of Justice League

app = Flask(__name__)

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent:Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]


@app.route("/")
def home():
    return "Hi"


@app.route("/normal")
def normal():
    return justice_league_members


@app.route("/jsonified")
def jsonified():
    return jsonify(justice_league_members)


if __name__ == "__main__":
    app.run(debug=True)
#################################################
# Flask Setup

#################################################
# @TODO: Initialize your Flask app here
# YOUR CODE GOES HERE

#################################################
# Flask Routes
#################################################

# @TODO: Complete the routes for your app here
# YOUR CODE GOES HERE

# if __name__ == "__main__":
#     app.run(debug=True)
#     # @TODO: Create your app.run statement here
#     # YOUR CODE GOES HERE

# app = Flask(__justice_league_members__)
# @app.route("/")
# def home():
#     print("Server received request for 'Home' page...")
#     return "Welcome to my 'Home' page!"