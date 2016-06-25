import requests


key = "a2cd9cdc7b9358e4156850f6e27ca339"
class Course:

	users = []
	num = None
	name = None
	

	def __init__(self, num, name):
    	self.num = num
    	self.name = name

    def addUser(self, user):
    	self.users.append(user)

    def update():
    	data = requests.get('https://api.uwaterloo.ca/v2/'self.name+'/'+self.num+'.json?key='+key)
   	    courseresponse = urllib.urlopen(data)
        coursedata = json.load(response)



   	# For every user subscribed.
   	def message_send():



   	def 
