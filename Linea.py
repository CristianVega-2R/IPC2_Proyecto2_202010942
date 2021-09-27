class Linea:
    def __init__(self, numero, componentes,tiempo):
        self.numero=numero
        self.componentes=componentes
        self.tiempo=tiempo

    def __str__(self):
        return str(self.numero)+ ", " +str(self.componentes) + ", " + str(self.tiempo)

    """metodos set"""
    def setNumero(self,numero):
        self.numero=numero

    def setComponentes(self,componentes):
        self.componentes=componentes

    def setTiempo(self, tiempo):
        self.tiempo=tiempo


    """metodos get"""
    def getNumero(self):
        return self.numero

    def getComponentes(self):
        return self.componentes

    def getTiempo(self):
        return self.tiempo

