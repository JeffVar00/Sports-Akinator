from arbol import Arbol
from nodo import Nodo

#  METODO GUARDAR E INSERTAR INFLUENCIADOS POR ESTE CODIGO https://ideone.com/FEYIfO

def perder(nodoActual):
    datoActual = nodoActual.dato()
    print("Buena esa, CracK")
    if datoActual[0] == 'P':
        datoHijo = input("Que personaje era?: ")
        datoPadre = input("Digite una frase que diferencia a su personaje: ")
        nodoActual._derecha = Nodo('P' + datoPadre)
        nodoActual.derecha()._izquierda = Nodo('R' + datoHijo)
        nodoActual.derecha()._derecha = Nodo('R' + "None")
    else:
        datoHijo = input("Que personaje era?: ")
        datoPadre = input("Digite una frase que diferencia a su personaje: ")
        nodoActual._dato = 'P' + datoPadre
        nodoActual._izquierda = Nodo('R' + datoHijo)
        nodoActual._derecha = Nodo('R' + datoActual)


def jugar(aquinator, opcion=None, nodoActual=None):
    seguir = False
    nodo = aquinator.obtener(opcion, nodoActual)
    if nodo is False:
        perder(nodoActual)
    elif nodo is True:
        print("Te adivine que era, mas respeto CRACK")
    elif nodo.dato() == "RNone":
        perder(nodoActual)
    else:
        while seguir is False:
            opcion = input("¿Su personaje es " + nodo.dato()[1:len(nodo.dato())] + "?" + " Acerte? S/N: ")
            opcion = opcion.upper()
            if opcion in ["S", "N"]:
                seguir = True
            else:
                print("Caracteres validos: S o N")
        jugar(aquinator, opcion, nodo)


def main():
    seguir = True
    preguntasyrespuestas = []
    with open('preguntasyrespuestas.txt', 'r') as fichero:
        for linea in fichero:
            preguntasyrespuestas.append(linea.rstrip())

    preguntasyrespuestas.reverse()

    aquinator = Arbol(preguntasyrespuestas)

    print("----------------AQUINATOR-----------------")
    while seguir:
        jugar(aquinator)
        opcion = input("Desea seguir jugando? S/N: ")
        if opcion == "N":
            seguir = False

    aquinator.guardar()


if __name__ == '__main__':
    main()
