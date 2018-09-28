def myName():
    return "Christopher"

def myFav():
    return "black"

def myHobby():
    return "bakestball"

def c2f(cTemp):
    fTemp = ((cTemp * 9 / 5) + 32)
    return fTemp

def maxNum(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c

def lowNum(a, b, c):
    if(a < b and a < c):
        return a
    elif(b < a and b < c):
        return b
    else:
        return c

def add(a, b):
    return a+b

print(myName())
print(c2f(0))
print(maxNum(10, 20, 10))
print(lowNum(10, 20, 50))

print(add(maxNum(1, 2, 3), lowNum(4, 5, 6)))