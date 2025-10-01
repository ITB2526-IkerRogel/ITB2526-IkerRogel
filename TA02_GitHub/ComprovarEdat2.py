import datetime


dataAtual = datetime.date.today()
anyActual = dataAtual.year
mesActual = dataAtual.month
print(dataAtual)
print(anyActual)

anyNeixament=int(input("Any de neixament?"))
mesNeixament = int(input("Mes neixament?"))

if (anyActual - anyNeixament) >=18:
    if mesNeixament <= mesActual:
        print("Ets major d'edat")
else:
    print("Ets menor")
print("Fi del programa")

