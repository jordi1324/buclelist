pal=int(input("Escriba las palabras que quiera que tenga la lista: "))
lista=[]#La primera lista (int)
lista2=[]#La segunda lista (int)
lista3=[]#La que aparecen en las dos listas
lista4=[]#Las que aparecen en la primera lista
lista5=[]#Las que aparecen en la segunda lista
lista6=[]#Todas las palabras


if(pal<0):
    print ("impossible ")
else:
    for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]
print(f"la lista es {lista}")
        
pal2=int(input("Escriba las palabras que quiera que tenga la lista: "))
for n in range(0,pal2):
        print(f"Digame la palabra {n+1}")
        palabra1=input()
        lista2+=[palabra1]
print(f"la lista es {lista2}")


lista3.append(set(lista) & set(lista2))#Esta parte filtra las palbras de las dos listas y mete en lista3 las coincidencias.
print(f"Las palabras que aparecen en las dos listas {lista3}")

for c in lista:
     if c not in (lista2):#Este bucle comprueba que  las palbras de la lista no aparecan en la lista2
          lista4.append(c)
print(f"Las palabras que solo aparecen en la primera lista {lista4}")

for c in lista2:
     if c not in (lista):
          lista5.append(c)
          print(f"Las palabras que solo aparecen en la segunda lista {lista5}")

lista6=lista3+lista4+lista5
print(f"Todas las palabras son {lista6}")

