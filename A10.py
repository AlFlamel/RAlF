import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Сколько штук?..")
x = int(input())
print("Сколько штукенций?..")
y = int(input())

x *= 75
y *= 112
z = x + y

print("Общая масса: " + str(z) + "г.")

printTimeStamp("Alexey.")