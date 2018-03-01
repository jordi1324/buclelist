pal=int(input("Escriba las palabras que quiera que tenga la lista: "))
lista=[]#La primera lista (int)
lista2=[]#La segunda lista (int)
lista3=[]#La que aparecen en las dos listas
lista4=[]#Las que aparecen en la primera lista
lista5=[]#Las que aparecen en la segunda lista
lista6=[]#Todas las palabras.

if(pal<0):
    print ("impossible ")
else:
    for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]
print(f"la lista es {lista}")
        
pala=int(input("Escriba las palabras que quiera que tenga la lista: "))
for a in range(0,pala):
        print(f"Digame la palabra {a+1}")
        palabra1=input()
        lista2+=[palabra1]
print(f"la lista es {lista2}")

for l in lista1:
    in l in lista2:
        lista7.append(l)

for i  in lista,lista2:
    if i in  (lista,lista2):
        lista3.append(i)
print(f"Las palabras que aparecen en las dos listas son{lista3}")

for z in (lista,lista2):
    if z not in lista2:
        lista4.append(z)
        print(f"La que solo aparecen en la primera {lista4}")

for x in (lista,lista2):
    if x not in lista:
        lista5.append(x)
        print(f"La que solo aparecen en la primera {lista5}")

for d in (lista,lista2):
        lista6.append(d)
        print(f"Todas las palabras{lista6}")

        
