import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.logging import default_handler

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

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

# Register the blueprints
from project.stocks import stocks_blueprint
from project.users import users_blueprint

app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
