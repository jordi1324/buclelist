pal=int(input("Escriba las palabras que quiera que tenga la lista: "))
lista=[]
pa1=0
pa2=0
na=0


if(pal<0):
    print ("impossible ")
else:
    for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]

print(f"La lista creada es:{lista}")

pa1=input("Escriba la palabra que va a substituir: ")
pa2=input("Por la palabra: ")

count=lista.count(pa1)
for i in range(count):
    na=lista.index(pa1)
    lista[na]=pa2


print(f"La lista es  ahora {lista}")




