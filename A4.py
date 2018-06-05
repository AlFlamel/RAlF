import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Enter the letter: ")
letter = str(input())
aletter = "aeiou"
ints = "1234567890"
if letter in aletter:
  print("Голосна.")
elif letter == "y":
  print("Голосна або приголосна.")
elif letter in ints:
  print("Цифра.")
else:
  print("Приголосна.")

printTimeStamp("Alexey.")