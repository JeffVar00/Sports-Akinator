from nodo import Nodo


class Arbol:

    def __init__(self, listaPreguntas, raiz=None, actual=None):
        self._raiz = raiz
        self._actual = actual
        self._raiz = self.insertarNodos(listaPreguntas)

    def insertarNodos(self, listaPreguntas):
        if len(listaPreguntas) != 0:
            aux = listaPreguntas.pop()
            if aux == "":
                return None
            nodoA = Nodo(aux)
            if aux[0] == 'P':
                nodoA._izquierda = self.insertarNodos(listaPreguntas)
                nodoA._derecha = self.insertarNodos(listaPreguntas)
            return nodoA
        else:
            return None

    def obtener(self, respuesta=None, nodoActual=None):

        if nodoActual is None:
            nodoActual = self._raiz
            return nodoActual

        if respuesta == "S" or respuesta == "s":
            if nodoActual.izquierda() is None:
                return True
            else:
                return nodoActual.izquierda()
        elif respuesta == "N" or respuesta == "n":
            if nodoActual.derecha() is None:
                return False
            else:
                return nodoActual.derecha()

        return "none"

    def guardar(self):
        fichero = open('preguntasyrespuestas.txt', 'w')
        linea = []
        self.guardarArbol(linea, self._raiz)
        fichero.writelines(linea)
        fichero.close()

    def guardarArbol(self, lista, nodo):
        if nodo.izquierda():
            lista.append(nodo.dato() + "\n")
            self.guardarArbol(lista, nodo.izquierda())
            self.guardarArbol(lista, nodo.derecha())
        else:
            lista.append(nodo.dato() + "\n")


"""
    def verArbol(self):
        self.verSubArbol(self._raiz)

    def verSubArbol(self, nodo):
        print("\n" + nodo.dato())
        if nodo.izquierda():
            print("S ")
            self.verSubArbol(nodo.izquierda())
        if nodo.derecha():
            print("N ")
            self.verSubArbol(nodo.derecha())
"""
