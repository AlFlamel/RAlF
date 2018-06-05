import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now()))

print("Введите числа: ")
n = input()
summ = 0
for i in n:
  if i in ['1','2','3','4','5','6','7','8','9']:
    summ += int(i)
print("Сума чисел: " + str(summ))

printTimeStamp("Alexey.")