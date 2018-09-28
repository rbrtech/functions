def todaysDate(month, date, year):
    print("Today is", month, date, year)


def farenheit2celcius(fTemp):
    cTemp = ((fTemp - 32) * 5/9)
    print(fTemp, "in Farenheight equals", cTemp, "in Celcius")

def celcius2farenheit(cTemp):
    fTemp = ((cTemp * 9 / 5) + 32)
    print(cTemp, "in Celcius equals", fTemp, "in Farenheight")

def ageCalc(month, date, year):
    if (month < 9):
        myAge = 2018 - year
    else:
        myAge = 2018 - (year+1)
    print("My birthday is", month, "/", date, "/", year, "and I'm", myAge, "years old!")


todaysDate("September", 24, 2018)
farenheit2celcius(32)
celcius2farenheit(0)


ageCalc(7, 21, 1987)
