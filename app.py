#!flask/bin/python

import flask
from flask import Flask

from dotenv import load_dotenv

load_dotenv()

import os

DEFAULT_IP_ADRESS = '127.0.0.1'
DEFAULT_PORT = '2000'

app = Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('index.html')

if __name__ == '__main__':
	#app.run(debug=True, host=os.getenv('IP_ADRESS', DEFAULT_IP_ADRESS),   \
	#	  port=os.getenv('PORT', DEFAULT_PORT))
	print(os.getenv('IP_ADRESS', DEFAULT_IP_ADRESS))
	print(os.getenv('PORT', DEFAULT_PORT))
	app.run(debug=True, host=DEFAULT_IP_ADRESS,   \
		  port=DEFAULT_PORT)

