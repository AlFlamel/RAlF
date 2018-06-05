import datetime

def printTimeStamp(name): 
  print('Автор програми: ' + name) 
  print('Час компіляції: ' + str(datetime.datetime.now()))

#31-Jan, 28-29-Feb, 31-Mar, 30-Apr, 31-May, 30-Jun, 31-Jul, 31-Aug, 30-Sep, 31-Oct, 30-Nov, 31-Dec.

month = input("Enter the month: ")

if month in ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]:
  print("31 day in " + month)
elif month in ["Apr", "Jun", "Sep", "Nov"]:
  print("30 day in " + month)
elif month in ["Feb"]:
  x = str(input("28 or 29 days?"))
  if x == "28":
    print("28 day in " + month)
  elif x == "29":
    print("29 day in " + month)
  else:
    print("Error 88234764520xgttr...")
else:
  print("Month error...")

printTimeStamp("Alexey.")