from flask import Flask, request
import requests
import os
import sys
import json
import traceback
import random
import urllib
from course import Course

app = Flask(__name__)

key = "a2cd9cdc7b9358e4156850f6e27ca339"
token = "EAAWx45TcH2oBAG7oZAtIoljLsiyQ8rrOlZC1LdXoaAEKau5YBfhrR5LLJnWegJ5VZAlRj98hm4xa2SIBg67aKYpqZBFwvWJAzD8pJ01zxR4qF8HaRXBDWsvZAIrZAZABsADJqfG537eEREziF87b5d1vnkNZCBF7sUBaLHsTCxul5wZDZD"
totalcourses = []

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            sys.stdout.write("Got data!")
            sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
            text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
            sys.stdout.write('got text and sender\n')
            courseinfo = text.split()
            payload = {'recipient': {'id': sender}, 'message': {'text': "You have selected:" + courseinfo[0] + " " + courseinfo[1] +". Retrieving data!" }}
            sys.stdout.write(courseinfo[0])
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)

            flag = 0
            for c in totalcourses:
                if text == c.title:
                    flag = 1
            if flag == 0:
                totalcourses = totalcourses.append(Course(courseinfo[0], courseinfo[1]))

            for c in totalcourses:
                if c.title == text:
                    returntext = c.update()

            returntext = "The course title is:" + coursedata['data']['title']
            payload = {'recipient': {'id': sender}, 'message': {'text': returntext }} # We're going to send this back
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
        except Exception as e:
            print traceback.format_exc() # something went wrong
        return "ok"
    elif request.method == 'GET': # For the initial verification
        if request.args.get('hub.verify_token') == 'enghack':
            return request.args.get('hub.challenge')
        return "Wrong Verify Token"
    return "Hello World" #Not Really Necessary

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
