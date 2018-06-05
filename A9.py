import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Сколько вам лет?"))
def years(a):
  if(a < 1):
    print("Вы ещё не народились. (Введено отрицательное число или ноль)")
    return
  elif(a >= 1):
    x1 = 2
    x2 = a - 2
    y1 = x1 // 10.5
    y2 = x1 // 4
    y3 = x2 // 7
    y4 = y2 + y3
    y5 = y1 + y3
    print("В собачьих годах вам: " + str(y4) + " лет.")
    print("В собачьих годах вам: " + str(y5) + " лет.")

years(a)

printTimeStamp("Alexey.")