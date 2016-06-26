import urllib

class Course:
    title = None
    users = []
    num = None
    name = None

    def __init__(self, num, name):
        self.num = num
        self.name = name
        self.title = name + " " + num

    def addUser(self, user):
        self.users.append(user)


    def update(self):
        getcoursesurl = 'https://api.uwaterloo.ca/v2/courses/'self.name+'/'+self.num+'.json?key='+key
        courseresponse = urllib.urlopen(getcoursesurl)
        coursedata = json.load(courseresponse)
