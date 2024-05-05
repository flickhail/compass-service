#!flask/bin/python

import flask
from flask import Flask

from dotenv import load_dotenv

load_dotenv()

import os

DEFAULT_IP_ADDRESS = '127.0.0.4'
DEFAULT_PORT = '5000'

app = Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('index.html')

if __name__ == '__main__':
	# debugging dotenv module
	print(os.getenv('IP_ADDRESS', DEFAULT_IP_ADDRESS))
	print(os.getenv('PORT', DEFAULT_PORT))

	app.run(debug=True, host=os.getenv('IP_ADDRESS', DEFAULT_IP_ADDRESS),   \
		  port=os.getenv('PORT', DEFAULT_PORT))
 
	#app.run(debug=True, host=DEFAULT_IP_ADDRESS,   \
	#	  port=DEFAULT_PORT)

