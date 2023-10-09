

app = Flask(__name__)

@app.route('/')
def guessnum():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src = "https://media1.giphy.com/media/'
            'fDUOY00YvlhvtvJIVm/giphy.gif?cid=ecf05e47n2syahkfqy96btxp'
            '48zp9yqs8y6c392drlimtl0i&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>')

@app.route('/<int:number>')
def user_guess(number):
    if number > randomNum:
        return ("<h2>Too high</h2>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    elif number < randomNum:
        return ("<h2>Too Low</h2>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    else:
        return ("<h2>You Guessed it</h2>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")


if __name__ == "__main__":
    app.run(debug=True)


