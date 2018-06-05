import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))				 

now = datetime.datetime.now() # Час
time = int(now.year)  # Рік
time = int(input("Enter year: "))
TextTime = str(time) # Число в строку
n1 = time % 400 # Якщо націло ділиться - Високосний	
n2 = time % 4   # З решти всі роки, що діляться на 4, є високосними.
n3 = time % 100 # З решти всі роки, що діляться на 100 – невисокосні.


# Якщо False - цей рік націло не ділиться 
# Якщо True  - цей рік ділиться без остачі

print(n1)
print(n2)
print(n3)

# Високосний рік
if n1 == 0 :
	print('Данний рік високосний: '+ TextTime)
elif n3 == 0 :
	print('Данний рік  не високосний: ' + TextTime) 
elif n2 == 0 :
	print('Данний рік високосний: '+ TextTime)
else :
	print('Данний рік  не високосний: ' + TextTime)

printTimeStamp("Alexey.")