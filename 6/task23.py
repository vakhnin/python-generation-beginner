from math import ceil, floor, radians, sin, cos, tan

x_radians = radians(float(input()))

result = sin(x_radians) + cos(x_radians) + tan(x_radians)**2
print(result)

