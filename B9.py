import datetime

def printTimeStamp(name):									
 print('Автор програми: ' + name)						
 print('Час компіляції: ' + str(datetime.datetime.now()))			

path = input('Введіть номерний знак: ')
old_letters = path[0:3] 
old_numbers = path[3:7] 
new_numbers = path[0:4] 
new_letters = path[4:7]

old_x = old_letters.isupper()
old_y = old_numbers.isdigit()

new_x = new_numbers.isdigit()
new_y = new_letters.isupper()

if old_x == True and old_y == True:
	print('Цей номерний знак - старий')
elif new_x == True and new_y == True:
	print('Цей номерний знак - новий')
else:
	print('Неправельно введено номер, спробуйте по шаблону (ABC123 або 1234ABC)')

printTimeStamp("Alexey.")
