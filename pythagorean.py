from math import sqrt
pythagorean = int(input("Enter your pythagorean number: "))
for a in range(1, pythagorean + 1):
    for b in range(a, pythagorean + 1):
        c_squared = a**2 + b**2
        c = int(sqrt(c_squared))
        if c_squared - (c**2) == 0:
            print(str(a)+ ',' + str(b) + ',' +str(c))