import datetime
import time

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Enter the ISBN: ")
isbn = list(input())

if len(isbn) == 13:
  print("Checking...")
  time.sleep(1)
  print("The code is accepted. Getting Started...", "\n")
  sum = 0
  for i in range(0,12):
    symb = int(isbn[i])
    if(i%2):
      symb*=3
    sum+=symb
  act2 = sum % 10
  act3 = 10 - act2
  print(act3, "\n")
else:
  print("Error: Enter the correct code.")

printTimeStamp("Alexey.")