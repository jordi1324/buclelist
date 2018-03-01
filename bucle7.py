pal=int(input("Escriba las palabras que quiera que tenga la lista: "))
lista=[]

if(pal<0):
    print ("impossible ")
else:
    for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]

print(f"La lista creada es:{lista}")

lista_nueva = []
for i in lista:
    if i not in lista_nueva:
        lista_nueva.append(i)
print(f"{lista_nueva}")
