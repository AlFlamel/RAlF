a = int(input ("Введіть кількість секунд: "))
h = str(a//3600)
d = str(a//86400)
m = (a//60)%60
s = a%60
if m < 10:
    m = '0' + str( m)
else:
    m = str(m)
if s < 10:
    s = '0'+str(s)
else:
    s = str(s)

print(d +':' + m + ':' + s + ';' + h)
