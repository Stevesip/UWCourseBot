from flask import Flask, request
import requests
import json
import traceback
import random
import os


app = Flask(__name__)

token = "enghack"


@app.route("/")
def root():
	return "UWCourseBot"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            payload = {'recipient': {'id': sender}, 'message': {'text': "You sent:" + text }}
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            print traceback.format_exc()
    elif request.method == "GET":
        if request.args.get("hub.verify_token") == token:
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
