import datetime

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now()))  

n=input("Bведіть ваш зріст у сантиметрах")

n1= (int(n)%30.48)//2.54
n2= int(n)//30.48
N=n2/float(3.2)

print(n1,"Дюймів")
print(n2,"Футів")

printTimeStamp("Alexey.")