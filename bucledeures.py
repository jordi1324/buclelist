limlist=int(input("Diga cuantas palabras va a introducir: "))

if limlist < 1:
    print("¡Imposible!")
else:
    lista=[]
    for n in range(limlist):
        n=n+1
        print(f"Escriba la palambra{n}")
        palabra=input()
        lista+=[palabra]
    print(f"La lista creada es: {lista}")
        
        
