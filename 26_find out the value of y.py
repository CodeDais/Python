import math
x = int(input('Enter x value'))
n = int(input('Enter n value'))

if n == 1:
    y = 1+x
elif n == 2:
    y = 1+(x//n)
elif n == 3:
    y = 1+math.pow(x, n)
else:
    y = 1+(n*x)

print('y value is = ', y)
