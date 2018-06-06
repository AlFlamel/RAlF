import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now()))

print("Введіть тиск:")
a = float(input())
print("обем:")
b = float(input())
print("темрепература:")
c = float(input())
f = 8.314
b3 = b/1000
g = c + 273.15
n = (a*b3)/(f*g)
print("Моларна маса газу:{:.2f}".format(n))

printTimeStamp("Alexey.")
