import requests

from flask import Flask
from flask import render_template
obj = Flask(__name__)


@obj.route('/')
def home():
    return "hello"


@obj.route('/guess/<name>')
def guess(name):
    response_age = requests.get(url=f"https://api.agify.io?name={name}")
    r_age = response_age.json()
    age = r_age["age"]
    gender = (requests.get(url=f"https://api.genderize.io?name={name}").json())["gender"]
    return render_template("newIndex.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    obj.run(debug=True)

