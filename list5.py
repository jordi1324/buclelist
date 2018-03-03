pal=int(input("Escriba las palabras que quiera que tenga la lista: "))
lista=[]#La primera lista (int)
lista2=[]#La segunda lista (int)
lista3=[]

if(pal<0):
    print ("impossible ")
else:
    for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]
print(f"la lista es {lista}")
        
pal2=int(input("Escriba las palabras que quiere eliminar: "))
for n in range(0,pal2):
        print(f"Digame la palabra {n+1}")
        palabra1=input()
        lista2+=[palabra1]
print(f"La lista de palabras a eliminar es  {lista2}")

for c in lista2:
     while c in (lista):
          lista.remove(c)
print(f"La lista ahora es {lista}")
          
