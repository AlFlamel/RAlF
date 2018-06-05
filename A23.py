import datetime
import math

def printTimeStamp(name): 
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))

print("Введіть а")
a = int(input())

print("Введіть b")
b = int(input())

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print("%.2f" % math.log10(a))
print(a**b)

printTimeStamp("Alexey.")