from lib import *
#import pymongo
from flask import Flask, request
#from pymongo import MongoClient
import requests
import os
import sys
import traceback
import random
import json

app = Flask(__name__)

'''
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
'''

@app.route('/index', methods=['GET', 'POST'])
def index():
    message = 'Show me course info on CS246'
    url = 'https://api.wit.ai/message?v=20160526&q='
    headers = {"Authorization":"Bearer QDZ7H7NKPFEK5J3WUBSQ4DBTCMBAVGOX"}

    strbuf = ''
    returnList = []
    requestType = ''
    courseExists = ''

    for char in message:
        if (char == " "):
            strbuf = strbuf + '%20'
        else:
            strbuf = strbuf + char

    urlSend = url + strbuf

    r = requests.post(urlSend, headers=headers)
    response = r.json()

    try:
        requestType = response['entities']['requestinfo']
    except NameError:
        requestType = None

    try:
        courseExists = response['entities']['coursecode'][0]['value']
    except NameError:
        courseExists = None

    if courseExists != None:
        returnList = returnList.append(courseExists)
    else:
        temp = ''
        initial = response['_text']
        courseCode = initial.replace(response['entities']['requestinfo'][0]['value'], "")

        # might have to do more parsing here.
        returnList = returnList.append(courseCode)

    print (response)
    return(returnList, 200)





if __name__ == '__main__':
    #client = MongoClient('mongodb://coursebotadmin:admin123@ds031607.mlab.com:31607/coursebotinfo')
    #db = client.coursebotinfo
    #collection = db.UWCourseBot
    #port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=3000, debug=True, threaded=True);
