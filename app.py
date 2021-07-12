# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
from forms import *

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
app = Flask(__name__)


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('droneLink-index.html')
    # return render_template('index.html')
    # return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/about2.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)

    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)

    return render_template('forms/forgot.html', form=form)


@app.route('/contact')
def contact():
    return render_template('pages/contact_us.html')


@app.route('/quote', methods=['GET', 'POST'])
def quote():
    form = QuoteForm(request.form)
    return render_template('pages/quote.html', form=form)


# GET and POST requests
@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "This is the first POST request!"
    else:
        return 'You are probably using a GET request!'


# Error handlers.

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

# ----------------------------------------------------------------------------#
# Launch.
# ----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.debug = True
    app.run()

