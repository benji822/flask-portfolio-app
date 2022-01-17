import logging
from logging.handlers import RotatingFileHandler

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask.logging import default_handler

# from markupsafe import escape

app = Flask(__name__)
# Remove the default logger configure by flask
app.logger.removeHandler(default_handler)
app.secret_key = b'\xa2\xc2\x9e\x87P\xc8bv&0\xb3r`\xf4\x1d\x00\x95\x8f\x08E\x85\xe7\xc4\x97\xc0]\xa6\xa8\xb2\x1d %\xf6'

# Logging Configuration

file_handler = RotatingFileHandler(
    'flask-stock-portfolio.log', maxBytes=16384, backupCount=20)
file_formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Log that the Flask application is starting
app.logger.info('Starting the Flask Portfolio App...')


@app.route('/', methods=['GET'])
def index():
    app.logger.info('Calling the index() function.')
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    flash('Thanks for learning about this site!', 'info')
    return render_template('about.html', company_name='asyncology.io')
    # return render_template('about.html')


@app.route('/list_stocks/', methods=['GET'])
def list_stocks():
    return render_template('stocks.html')


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key}: {value}')

        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']
        flash(
            f'Added new stock ({ request.form["stock_symbol"] })!', 'success')
        app.logger.info(f'Added new stock ({ request.form["stock_symbol"] })!')
        return redirect(url_for('list_stocks'))

    return render_template('add_stock.html')


@app.route('/clock')
def clock():
    return 'Try HTMX'


if __name__ == '__main__':
    app.run(debug=True)
