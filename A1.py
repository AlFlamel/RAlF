import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now()))

print("Контейнери об’ємом до 1л?..")
m = float(input())
print("Контейнери об’ємом понад 1л?..")
b = float(input())

x = m * 0.10
y = b * 0.25
z = x+y
print(str("%.2f" % x) + "$" + " сума за кількість контейнерів об’ємом до 1л")
print(str("%.2f" % y) + "$" + " сума за кількість контейнерів об’ємом понад 1л")
print("Разом отримано: " + str("%.2f" % z) + "$")

printTimeStamp("Alexey.")