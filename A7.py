import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

v=input("Напишіть температуру у Цельсіях: ") 
v1=273 
v2=32 
print(str((v1) + int(v)) + " по Кельвiну") 
print(str((v2) + int(v)*1.8) + " по Фаренгейту")

printTimeStamp("Alexey.")