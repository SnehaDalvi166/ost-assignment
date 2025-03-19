import math
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))
# if a is 0,then incorrect equation
if a == 0:
    print("incorrect input, quadratic equation not possible")
else:
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    numer = math.sqrt(abs(dis))
    den=2*a
    # checking condition for discriminant
    if dis > 0:
        print("real and different roots")
        print((-b + numer)/(den))
        print((-b - numer)/(den))
    elif dis == 0:
        print("real and same roots")
        print(-b/(den))
    # when discriminant is less than 0
    else:
        print("complex roots or imaginary roots")
        print(-b / (den), " + i", numer)
        print(-b / (den), " - i", numer)

        
