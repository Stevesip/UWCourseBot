from flask import Flask, request
import requests
import json
import traceback
import random
import os
import sys


app = Flask(__name__)

token = "EAAWx45TcH2oBANaTOaFtRmWdBSSsY1XZBn9fZCVvIQ0IqZBN2Mn1k3HcCEvTZBlmI4q8zRUN9RyLbP9ylbMaIHRcQRDQIm0aqPRZB0ctZBlHsku3nzl5IiIFd1XmfsnLMzM390X91piLumhpPD3ObZAlgLjQLoFLS3ZA9HDOdgwZBTgZDZD"


@app.route("/")
def root():
	return "UWCourseBot"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook():
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            sys.stdout.write(data)
            text = data['entry'][0]['messaging'][0]['message']['text']
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            payload = {'recipient': {'id': sender}, 'message': {'text': text }}
            sys.stdout.write('recieved:' + text +  'attempting to write to the user')
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        except Exception as e:
            sys.stdout.write(traceback.format_exc())
    elif request.method == "GET":
        if request.args.get("hub.verify_token") == enghack:
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
