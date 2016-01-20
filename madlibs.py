from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_game_form():
    """Show game."""

    yes_no = request.args.get("yesno")

    if yes_no == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib') #when we go to /madlib, call this function  
def show_madlib():
    """show madlib result"""

    adj = request.args.getlist("adj")
    Adj = choice(adj)
    person_name = request.args.get("person_name")
    color_pick = request.args.get("color_pick")
    noun = request.args.get("noun")

    madlib_choices = ["madlib.html", "madlib2.html"]
    madlib_pick = choice(madlib_choices)

    return render_template(madlib_pick, 
                            Person=person_name, 
                            Color=color_pick,
                            Noun=noun,
                            Adjective=Adj)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)