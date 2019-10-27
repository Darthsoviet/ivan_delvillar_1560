
def se_puede(n):
    valoresImposibles = [0, 1, 2, 3, 4, 6, 7, 9, 11, 12, 14, 17, 19, 22, 27]
    if n in valoresImposibles:
        return False
    else:
        return True

def confirmar(n,x,y,z):
    if x*24+y*8+z*5==n:

        return True
    else:
        return False

def ciclos(n):  # lapices que desea el usuario
    x = 0
    z = 0
    y = 0
    sub=0
    sub1=0
    lista=[]
    while(not confirmar(n,x,y,z)):
        x=n//24
        while x >= 0:
            sub = n-x*24
            y = sub//8
            while y >= 0:
                sub1=sub-y*8
                z=sub1//5
                while z >=0:
                    if confirmar(n,x,y,z):
                        break
                    z-=1
                if confirmar(n, x, y, z):
                    break
                y-=1
            if confirmar(n, x, y, z):
                break
            x-=1
        lista.append(x)
        lista.append(y)
        lista.append(z)
        return lista

def completo():
    n=int(input("inserte un numero de lapices deseados"))
    if se_puede(n):
        l=ciclos(n)
        print(f"paquetes... 24 ={l[0]}|8= {l[1]}|5= {l[2]} ")
    else:
        print("cantidad imposible para los paquetes que tenemos")
completo()