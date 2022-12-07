a =[]
for i in range(10):
   x = int(input("Podaj liczbe"))
   a.append(x)
pozycja = -1
for j in range(10):
    print(a[pozycja])
    pozycja = pozycja -1
print(a)
print(max(a))

