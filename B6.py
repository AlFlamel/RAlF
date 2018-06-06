import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))	  			  

coin = (1,2,5,10,25,50)

print(coin[4])

printTimeStamp("Alexey.")
