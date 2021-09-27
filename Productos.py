from ListaEnlazada import ListaEnlazada

class Producto:
    def __init__(self, nombre, recetafake):
        self.nombre=nombre
        self.receta = ListaEnlazada()
        self.recetabackup = ListaEnlazada()
        for i in range(len(recetafake)-1):
            self.receta.Append(recetafake[i])
            self.recetabackup.Append(recetafake[i])


    def __str__(self):
        return str(self.nombre) +", " +str(self.receta)

    def getNombre(self):
        return self.nombre

    def getReceta(self):
        return self.receta

    def reset(self):
        print("se hace un reset")
        self.receta=self.recetabackup
