import json
import os
import sys
import traceback
import random

url = 'https://api.uwaterloo.ca/v2/courses/'
key = '2d91198533b55707eaf3e29850108000'

witUrl = ''
witKey = ''

# api call to https://api.uwaterloo.ca/v2/courses
def getAllCourses():
	r = requests.get(url + '.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

# api call to https://api.uwaterloo.ca/v2/courses/{SUBJECT}
def getCoursesBySubject(subject):
	r = requests.get(url + subject.upper() + '.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

# api call to https://api.uwaterloo.ca/v2/courses/{COURSEID}
def getCourseByID(course_id):
	r = requests.get(url + str(course_id) + '.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

# api call to https://api.uwaterloo.ca/v2/courses/{SUBJECT}/{CATELOG_NUMBER}
def getCourseByCatelogNumber(subject, catelog_num):
	r = requests.get(url + subject.upper() + '/' + str(catelog_num) + '.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

# api call to https://api.uwaterloo.ca/v2/courses/{SUBJECT}/{CATELOG_NUMBER}/schedule
def getCourseSchedule(subject, catelog_num):
	r = requests.get(url + subject.upper() + '/' + str(catelog_num) + '/schedule.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

# api call to https://api.uwaterloo.ca/v2/courses/{SUBJECT}/{CATELOG_NUMBER}/prerequisites
def getCoursePrerequisites(subject, catelog_num):
	r = requests.get(url + subject.upper() + '/' + str(catelog_num) + '/prerequisites.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

# api call to https://api.uwaterloo.ca/v2/courses/{SUBJECT}/{CATELOG_NUMBER}/examschedule
def getCourseExamSchedule(subject, catelog_num):
	r = requests.get(url + subject.upper() + '/' + str(catelog_num) + '/examschedule.json?key=' + key)
	if r.json()['meta']['status'] == 200:
		return r.json()['data']
	else:
		return

'''
# wit understanding
def parseMessage(message) {
	strbuf = ''

	for char in message:
		if (char == " "):
			strbuf = strbuf + '%20'
		else:
			strbuf = strbuf + char

	urlSend = url + strbuf

	r = requests.get(urlSend)
	#set header with authorization token

	rWit = json.loads(r.text)

	if ()
'''







