import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now()))

name = str(input("Как вас зовут?.."))
print("Здравствуйте " + name)

printTimeStamp("Alexey.")
