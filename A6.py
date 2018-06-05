import datetime 

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now())) 

i = float(input("Введіть вартість страв: ")) 

p = 18%i 
ch = 14%i 
t = i + p + ch 

print ("Податок становить : ", p) 
print ("Чайові: ", ch) 
print ("Загальна сума до сплати: ", t) 

printTimeStamp('Alexey.')