pal=int(input("Escribe cuantas palabras quieres que tenga la lista: "))
lista=[]
rem=0
for n in range(0,pal):
        print(f"Digame la palabra {n+1}")
        palabra=input()
        lista+=[palabra]

print(f"La lista es {lista}")

rem=input("La palabra a eliminar es: ")
count=lista.count (rem)

for i in range (count):
    lista.remove(rem)
print(f"La nueva lista es {lista}")
