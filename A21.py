import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now())) 

print("Ціле число: ") 
n = float(input()) 
s = (n*(n + 1))/2 

print ("Сума: ",s)

printTimeStamp("Alexey.")