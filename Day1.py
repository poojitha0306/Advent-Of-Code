import math
def CalculateMass():
    fuel = 0
    mass = open('Day1_input.txt','r')
    for i in mass:
        fuel = fuel + ((math.floor(int(i)/3))-2)
    print (fuel)

CalculateMass()