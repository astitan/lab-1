# 4. По сторонам треугольника вычислить площадь вписанного в него круга.
import math
print('Введите значения сторон треугольника')
a = int(input())
b = int(input())
c = int(input())
if (a>(b+c)) or (b>(a+c)) or (c>(a+b)):
    print('Такой треугольник не существует, введите корректные значения сторон')
p = (a+b+c) / 2
S1 = math.sqrt(p*(p-a)*(p-b)*(p-c))
r = S1/p
S2 = math.pi*math.pow(r,2)
print('Площадь вписанного круга в треугольник равна: ', S2)

