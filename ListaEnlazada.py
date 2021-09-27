
"""Clases para lista"""

class Nodo:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None

    def __str__(self):
        return str(self.Value)

    def getNombre(self):
        return str(self.Value.getNombre())

    def buscarBrazo(self, numero):
        return self.Value.buscarBrazo(numero)

    def getReceta(self):
        return self.Value.getReceta()

    def asignarMeta(self,dato):
        return self.Value.asignarMeta(dato)

    def tic(self,  receta):
        self.Value.tic(receta)


class ListaEnlazada:
    def __init__(self):
        self.First = None
        self.Size = 0

    """Método agregar elemento a lista"""
    def Append(self, Value):
        NodoNuevo = Nodo(Value)
        if self.Size==0:
            self.First = NodoNuevo
        else:
            Current = self.First
            while Current.Next != None:
                Current = Current.Next
            Current.Next = NodoNuevo
        self.Size += 1
        return NodoNuevo

    def Modificar(self, dato, id):
        Current = self.First
        contador = 0
        while contador < id:
            if Current.Next == None:
                return False
            else:
                Current = Current.Next
                contador += 1
        Current.Value=dato


    """Método remover elemento de la lista"""
    def Remove(self, id):
        if self.Size == 0:
            return False
        else:
            Current = self.First
            if id == 0:
                self.First=Current.Next
                self.Size-=1
            else:
                contador=0
                while contador != id - 1:
                    if Current.Next == None:
                        return False
                    else:
                        Current = Current.Next
                        contador += 1
                DeletedNode = Current.Next
                Current.Next = DeletedNode.Next
                self.Size-=1
                return DeletedNode


    """Retornar tamaño de lista"""
    def __len__(self):
        return self.Size

    """Retornar lista completa"""
    def __str__(self):
        String = "["
        Current = self.First

        while Current != None:
            String += "'"+str(Current)
            if Current.Next == None:
                String += str("']")
            else:
                String += str("', ")
            Current = Current.Next
        return String

    """Seleccionar item de la lista dado un Index"""
    def Seleccionar(self, id):
        Current = self.First
        contador = 0
        while contador < id:
            if Current.Next==None:
                return False
            else:
                Current = Current.Next
                contador+=1
        return Current

    def SeleccionarValor(self, id):
        Current = self.First
        contador = 0
        while contador < id:
            if Current.Next==None:
                return False
            else:
                Current = Current.Next
                contador+=1
        return Current.Value