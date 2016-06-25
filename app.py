from flask import Flask, request
import requests
import json
import traceback
import random
import os


app = Flask(__name__)

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
	if request.method == "GET":
		if request.args.get("hub.verify_token") == 'enghack':
			return request.args.get('hub.challenge')
		return "Wrong Verify Token"



#@app.route("")
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)