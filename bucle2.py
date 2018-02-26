pal=int(input("Escribe cuantas palabras quieres que tenga la lista: "))
lista=[]


if(pal<0):
    print ("impossible ")
else:
    for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]

li=input("Digame la palabra a buscar:" )
lista.count(li)

if(lista.count(li)==0):
    print("Esta palabra no esta")

if (lista.count(li)==1):
    print(f"La palabra {li} aparece en la lista una vez")
else:
    print(f"La palabra {li} aparece {lista.count(li)} en la lista")

