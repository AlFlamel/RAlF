import datetime
import math

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Довжина сторони: ")
s = float(input())
print("Кількість сторон: ")
n = float(input())
с = n*s**2
h = float(math.pi/n)
s = 4 * math.tan(h)

print ("Площа: ",s ,"см,квадрат")
 
printTimeStamp("Alexey.")
