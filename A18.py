import math
import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Введите высоту: ")
d = float(input()) # Высота.   м
vi = 0 # Начальная скорость.   м/с
a = 9.8 # Ускорение в падении. м/с2

vf = math.sqrt(float(pow(vi,2) + 2 * a * d))

print("Окончательная скорость: " + str(vf) + " м/с")

printTimeStamp("Alexey.")