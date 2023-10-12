from flask import Flask, render_template
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email
from flask import current_app, request
from werkzeug.urls import url_encode


class LoginMyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4)])
    # submit = SubmitField(label='LogIn')



app = Flask(__name__)
app.secret_key = "pythondev"

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginMyForm()
    login_form.validate_on_submit()
    # print(login_form.email.data)
    # print(login_form.password.data)
    ##########    OR    #################
    # if login_form.validate_on_submit() == True:
    #     print(login_form.email.data)
    #     print(login_form.password.data)
    ############   OR   #################
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
