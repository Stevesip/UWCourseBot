from flask import Flask, request
import requests
import os
import sys
import traceback
import random
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == 'uwcourse':
            return request.args.get('hub.challenge')
    elif request.method == 'POST':
        data = json.loads(request.data)
        sender = data['entry'][0]['messaging'][0]['sender']['id']

        if (len(data['entry'][0]['messaging']['message']['text']) == 0):
            #then we know that the user has requested something. Now this is where we need to extract the text and send it to wit.
            # based on what is returned. we send this method to wit.ai
            # the 'entity', from the json that is returned will guide us
            message = data['entry'][0]['messaging']['message']['text']

            # send to wit and get the return.
            # might want to make a helper send function.




if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
