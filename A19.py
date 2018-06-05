import datetime
import time

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))

t = time.localtime()
print(time.asctime(t))

printTimeStamp("Alexey.")