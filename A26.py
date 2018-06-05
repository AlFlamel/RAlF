import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Сторона a: ")
a = input()
print("Сторона b: ")
b = input()
print("Сторона c: ")
c = input()

if (a == b == c):
  print("Рівносторонній.")
elif (a == b !=c) or (a == c != b) or (b == c != a):
  print("Рівнобедрений.")
elif (a != b != c):
  print("Hерівносторонній.")
else:
  print("Error: Enter the correct values.")

printTimeStamp("Alexey.")