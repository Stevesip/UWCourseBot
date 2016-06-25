import requests


key = "a2cd9cdc7b9358e4156850f6e27ca339"
class Course:
	title = None
	users = []
	num = None
	name = None
	

	def __init__(self, num, name):
    	self.num = num
    	self.name = name
    	self.title = name + num

    def addUser(self, user):
    	self.users.append(user)

    def update(self):
    	data = requests.get('https://api.uwaterloo.ca/v2/'self.name+'/'+self.num+'.json?key='+key)
   	    courseresponse = urllib.urlopen(data)
        return json.load(response)



 