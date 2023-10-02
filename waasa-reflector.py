#!/usr/bin/python3

import os
import argparse
from flask import Flask

from app.views import views


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--listenip', type=str, help='IP to listen on', default="0.0.0.0")
	parser.add_argument('--listenport', type=int, help='Port to listen on', default=5002)
	parser.add_argument('--debug', action='store_true', help='Debug', default=False)
	args = parser.parse_args()

	root_folder = os.path.dirname(__file__)
	app_folder = os.path.join(root_folder, 'app')

	app = Flask(__name__, 
		static_folder=os.path.join(app_folder, 'static'),
		template_folder=os.path.join(app_folder, 'templates')
	)

	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.config['SECRET_KEY'] = os.urandom(24)
	app.config['SESSION_TYPE'] = 'filesystem'

	app.config.from_prefixed_env()
	app.register_blueprint(views)
	app.run(host=args.listenip, port=args.listenport, debug=args.debug)
