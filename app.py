import lib.py
import pymongo
from flask import Flask, request
from pymongo import MongoClient
import requests
import os
import sys
import traceback
import random
import json

app = Flask(__name__)

def enterOneEntry(senderId, message):
    if collection.find_one({"senderId": senderId}) != None:
        #Entry already found, just update
        result=collection.update_one({"senderId": senderId},{"message": message})
        if result.acknowledged == False:
            # Didnt work, post error
        else:
            # Worked
    else:
         result=collection.insert_one({"senderId": senderId,"message": message})
         if result.acknowledged == False:
             # Didnt work, post error
         else:
             # Worked

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
    client = MongoClient('mongodb://coursebotadmin:admin123@ds031607.mlab.com:31607/coursebotinfo')
    db = client.coursebotinfo
    collection = db.UWCourseBot
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
