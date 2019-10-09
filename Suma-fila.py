def Suma(lista):

    suma=lista[0]
    lista2=lista[1:]
    if len(lista)==1:
        return suma
    else:

        return suma+Suma(lista2)

def main():
    print(“—————————————-“)
    lista=[4,2,5,6,2,4]
    print(f”{suma_lista(lista)}”)

main()
