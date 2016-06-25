from flask import Flask, request
import json
<<<<<<< HEAD
=======
#import requests
>>>>>>> origin/master
import traceback
import random
import os


app = Flask(__name__)

<<<<<<< HEAD
token = "enghack"
=======
>>>>>>> origin/master


@app.route("/")
def root():
	return "UWCourseBot"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
<<<<<<< HEAD
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            payload = {'recipient': {'id': sender}, 'message': {'text': "You sent:" + text }}
             r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    elif request.method == "GET":
=======
	if request.method == "POST":
		data = json.loads(request.data)
		print (data)

	if request.method == "GET":
>>>>>>> origin/master
		if request.args.get("hub.verify_token") == 'enghack':
			return request.args.get('hub.challenge')
		return "Wrong Verify Token"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
<<<<<<< HEAD
	app.run(host='0.0.0.0', port=port)
=======
	app.run(host='0.0.0.0', port=port)
>>>>>>> origin/master
