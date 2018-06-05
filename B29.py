import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

def fact(n):
  factors = []
  d = 2
  m = n # Запомним исходное число

  if(m < d):
    print("Error: Enter a valid number.")
    return 0
  else:
    while (d * d <= n) and (m >= 2):
      if n % d == 0:
        factors.append(d)
        n //= d
      else:
        d += 1

  factors.append(n) # Добавим последнеё простое число
  print('{} = {}' .format(m, factors)) # Выводим исходное число и все простые множители.

n = int(input("Число: "))

fact(n)

printTimeStamp("Alexey.")