import math

x = input().split("' '")
y = input().split("' '")

x1, x2 = x
y1, y2 = y

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2) - float(y1))*(float(y2) - float(y1))))

print('%0.4f'%distancia)