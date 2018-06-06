import datetime

def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))	  

print("Місце проживання (Гуртожиток, Квартира, Будинок)")
home = input("Введіть місце проживання: ")

time = int(input("Введіть скільки годин ви приблизно знаходитесь дома: "))

if(home == "Гуртожиток") and (time < 6):
	print("Тобі підійде: Мурашник")
elif(home == "Гуртожиток") and (time == 6):
  print("Тобі підійде: Мурашник або рибки")
elif(home == "Гуртожиток") and (time > 6):
  print("Тобі підійдуть: Рибки")
elif(home == "Квартира") and (time < 10):
  print("Тобі підійде: Хом'як")
elif(home =="Квартира") and (time == 10):
	print("Тобі підійде: Хом'як або Кішка")
elif(home =='Квартира') and (time > 10):
	print('Тобі підійде: Кішка')
elif(home =='Будинок') and (time <= 10):
	print("Тобі підійде: Змія")	
elif(home =='Будинок') and (time > 10) and (time < 17):
	print("Тобі підійде: Собака")
elif (home =='Будинок') and (time > 18):
	print("Тобі підійде: В’єтнамське порося")

printTimeStamp("Alexey.")
