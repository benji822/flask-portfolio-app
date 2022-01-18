from flask import (current_app, flash, redirect, render_template, request,
                   session, url_for)
from project import database as db
from project.models import Stock

from . import stocks_blueprint


@stocks_blueprint.before_request
def stocks_before_request():
    current_app.logger.info('Calling before_request() for the stocks blueprint...')


@stocks_blueprint.after_request
def stocks_after_request(response):
    current_app.logger.info('Calling after_request() for the stocks blueprint...')
    return response


@stocks_blueprint.teardown_request
def stocks_teardown_request(error=None):
    current_app.logger.info('Calling teardown_request() for the stocks blueprint...')


@stocks_blueprint.route('/')
def index():
    current_app.logger.info('Calling the index() function...')
    return render_template('stocks/index.html')


@stocks_blueprint.route('/stocks/', methods=['GET'])
def list_stocks():
    stocks = Stock.query.order_by(Stock.id).all()
    return render_template('stocks/stocks.html', stocks=stocks)


@stocks_blueprint.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        new_stock = Stock(
            request.form['stock_symbol'],
            request.form['number_of_shares'],
            request.form['purchase_price']
        )
        db.session.add(new_stock)
        db.session.commit()

        flash(f'Added new stock ({ request.form["stock_symbol"] })!', 'success')
        current_app.logger.info(f'Added new stock ({ request.form["stock_symbol"] })!')
        return redirect(url_for('stocks.list_stocks'))

    return render_template('stocks/add_stock.html')
