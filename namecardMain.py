from flask import Flask
from flask import render_template
obj = Flask(__name__)


@obj.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    obj.run(debug=True)

