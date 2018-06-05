import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now())) 

print("1. Зріст вимірюється в дюймах, а маса – у фунтах.")
print("2. Зрiст вимірюється в метрах, а маса – у кiлограмах.")
mtd = input()

if mtd == "1":
  x = float(input("Зріст: "))
  y = float(input("Маса: "))
  IMT1 = 703.0 * y / pow(x,2)
  print("IMT = " + "%.2f" % IMT1)
elif mtd == "2":
  x = float(input("Зріст: "))
  y = float(input("Маса: "))
  IMT2 = y / pow(x,2)
  print("IMT = " + "%.2f" % IMT2)
else:
  print("Error: Option is not correct. Use 1 or 2.")

printTimeStamp("Alexey.")