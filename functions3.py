x = 50
y = 60
z = 70

print("global x is", x)
print("global y is", y)
print("global z is", z)
print("---------------------")

def xFuction():
    x = 5
    print("local x is", x)


def yFunction():
    y = 6
    print("local y is", y)


def zFunction():
    z = 7
    print("local z is", z)


def xChange(num1):
    global x
    x = num1
    print("new local x is", x)
    print("new global x is", x)


def yChange(num2):
    global y
    y = num2
    print("new local y is", y)
    print("new global y is", y)


def zChange(num3):
    global z
    z = num3
    print("new local z is", z)
    print("new global z is", z)

xFuction()
yFunction()
zFunction()

print("---------------------")

xChange(123)
yChange(456)
zChange(789)

print("---------------------")

print("global x is", x)
print("global y is", y)
print("global z is", z)