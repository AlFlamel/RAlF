import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

max_ = 10

for row in range(1, max_ + 1):
  for column in range(1, max_ + 1):
    print(row * column, end='\t')
  print()

printTimeStamp("Alexey.")