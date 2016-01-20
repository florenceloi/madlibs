from random import choice, sample

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

    return render_template("home.html")


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment_list = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliment_list)


@app.route('/game')
def show_game_form():
    """Show game."""

    yes_no = request.args.get("yesno")

    if yes_no == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib', methods=["POST"]) #when we go to /madlib, call this function  
def show_madlib(): 
    """show madlib result"""

    adj = request.form.getlist("adj")
    Adj = choice(adj)
    print Adj, "LOOK HERE"
    person_name = request.form.get("person_name")
    color_pick = request.form.get("color_pick")
    noun = request.form.get("noun")
    scenario = request.form.get("Scenario")
 
    return render_template("madlib.html",
                            Scenario=scenario, 
                            Person=person_name, 
                            Color=color_pick,
                            Noun=noun,
                            Adjective=Adj)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
