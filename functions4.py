name = ""
verb = ""
place = ""
food = ""

def name(a):
    global name
    name = a

def verb(b):
    global verb
    verb = b

def place(c):
    global place
    place = c

def food(d):
    global food
    food = d

def myStory():
    print(name, verb, "to", place, "and ate a", food)

name("Mike")
verb("ran")
place("store")
food("pizza")

myStory()