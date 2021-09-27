class Brazo:
    def __init__(self, numero, componentes, tiempo):
        self.numero=numero
        self.componentes=componentes
        self.tiempo=tiempo
        self.tiempoaux=tiempo
        self.posActual=0
        self.meta= "C0"
        self.prioridad=None

    def __str__(self):
        return str(self.numero) + ", " + str(self.componentes) + ", " + str(self.tiempo)


    def buscarBrazo(self, numero):
        if self.numero == numero:
            return True
        else:
            return False

    def asignarMeta(self, meta):
        self.meta=meta
        return self

    def tic(self, receta,prioridad,cola, tabla, segundos):
        for i in range(0,len(cola),2):
            if str(cola.SeleccionarValor(i))== "L"+str(self.numero) and str(cola.SeleccionarValor(i+1)) == str(self.meta):
                self.prioridad=i
        if self.posActual < int(str(self.meta).replace("C","")):
            self.posActual+=1

            tabla.insert("", 0,text="El brazo " + str(self.numero) + " se movió al componente " + str(self.posActual),values=segundos)

        elif self.posActual > int(str(self.meta).replace("C","")):
            self.posActual-=1

            tabla.insert("", 0, text="El brazo " + str(self.numero) + " retrocedió al componente " + str(self.posActual), values=segundos)

        elif str(self.meta) == "C"+str(self.posActual) and prioridad == self.prioridad:

            tabla.insert("", 0, text="El brazo " + str(self.numero) + " está ensamblando el componente " + str(self.posActual) + ",tiempo restante: " + str(self.tiempo), values=segundos)

            self.tiempo -= 1
            if self.tiempo == 0:
                self.tiempo = self.tiempoaux
                for i in range(0, len(receta), 2):
                    if ("L" + str(self.numero) == str(receta.Seleccionar(i))):
                        self.meta = receta.Seleccionar(i + 1)

                        tabla.insert("", 0, text="Se terminó de ensamblar próximo ensamblaje en: " + str(receta.Seleccionar(i + 1)),values=segundos)

                        receta.Remove(i)
                        receta.Remove(i)
                        return receta

                tabla.insert("", 0,text="Se terminó de ensamblar no hay más ensamblajes en este brazo", values=segundos)

                self.posActual=0
                self.meta = "C0"
                self.prioridad=None
                receta.Append("XD")
                return receta
        else:
            tabla.insert("", 0, text="Brazo " + str(self.numero) + " hace nada", values=segundos)

        return receta


    def ticHTML(self, receta,prioridad,cola, fila, segundos):

        for i in range(0,len(cola),2):
            if str(cola.SeleccionarValor(i))== "L"+str(self.numero) and str(cola.SeleccionarValor(i+1)) == str(self.meta):
                self.prioridad=i
        if self.posActual < int(str(self.meta).replace("C","")):
            self.posActual+=1

            fila.write("<td>El brazo " + str(self.numero) + " se movio al componente " + str(self.posActual) + "</td>\n<td>"+str(segundos)+"</td>\n")

        elif self.posActual > int(str(self.meta).replace("C","")):
            self.posActual-=1

            fila.write("<td>El brazo " + str(self.numero) + " retrocedio al componente " + str(self.posActual)+"</td>\n<td>" +str(segundos) + "</td>\n")


        elif str(self.meta) == "C"+str(self.posActual) and prioridad == self.prioridad:

            fila.write("<td>El brazo " + str(self.numero) + " esta ensamblando el componente " + str(self.posActual) + ",tiempo restante: " + str(self.tiempo) + "</td>\n<td>" +str(segundos)+"</td>\n")


            self.tiempo -= 1
            if self.tiempo == 0:
                self.tiempo = self.tiempoaux
                for i in range(0, len(receta), 2):
                    if ("L" + str(self.numero) == str(receta.Seleccionar(i))):
                        self.meta = receta.Seleccionar(i + 1)


                        fila.write("<td>Se termino de ensamblar proximo ensamblaje en: " + str(receta.Seleccionar(i + 1))+"</td>\n<td>"+str(segundos)+"</td>\n")

                        receta.Remove(i)
                        receta.Remove(i)
                        return receta

                fila.write("<td>Se termino de ensamblar no hay más ensamblajes en este brazo</td>\n<td>"+ str(segundos)+"</td>\n")

                self.posActual=0
                self.meta = "C0"
                self.prioridad=None
                receta.Append("XD")
                return receta
        else:
            fila.write("<td>Brazo " + str(self.numero) + " hace nada</td>\n<td>" + str(segundos)+"</td>\n")

        return receta

    def ticXML(self, receta,prioridad,cola, file):
        for i in range(0,len(cola),2):
            if str(cola.SeleccionarValor(i))== "L"+str(self.numero) and str(cola.SeleccionarValor(i+1)) == str(self.meta):
                self.prioridad=i
        if self.posActual < int(str(self.meta).replace("C","")):
            self.posActual+=1

            file.write("\n\t\t\t\t\t<LineaEnsamblaje NoLinea=\""+ str(self.numero) + "\">\n\t\t\t\t\t\tEl brazo se movió al componente " + str(self.posActual)+"\n\t\t\t\t\t</LineaEnsamblaje>")


        elif self.posActual > int(str(self.meta).replace("C","")):
            self.posActual-=1

            file.write("\n\t\t\t\t\t<LineaEnsamblaje NoLinea=\""+ str(self.numero) + "\">\n\t\t\t\t\t\tEl brazo retrocedió al componente " + str(self.posActual)+"\n\t\t\t\t\t</LineaEnsamblaje>")


        elif str(self.meta) == "C"+str(self.posActual) and prioridad == self.prioridad:

            file.write("\n\t\t\t\t\t<LineaEnsamblaje NoLinea=\""+ str(self.numero)+"\">\n\t\t\t\t\t\t El brazo " + str(self.numero) + " está ensamblando el componente " + str(self.posActual) + ", tiempo restante: " + str(self.tiempo)+"\n\t\t\t\t\t</LineaEnsamblaje>")


            self.tiempo -= 1
            if self.tiempo == 0:
                self.tiempo = self.tiempoaux
                for i in range(0, len(receta), 2):
                    if ("L" + str(self.numero) == str(receta.Seleccionar(i))):
                        self.meta = receta.Seleccionar(i + 1)


                        file.write("\t\t\t\t\t<LineaEnsamblaje NoLinea=\"" + str(self.numero) + "\">\n\t\t\t\t\t\t" + "Se terminó de ensamblar próximo ensamblaje en: " + str(receta.Seleccionar(i + 1))+"\n\t\t\t\t\t</LineaEnsamblaje>")
                        receta.Remove(i)
                        receta.Remove(i)
                        return receta

                file.write("\n\t\t\t\t\t<LineaEnsamblaje NoLinea=\"" + str(self.numero) + "\">\n\t\t\t\t\t\t" +"Se terminó de ensamblar no hay más ensamblajes en este brazo\n\t\t\t\t\t</LineaEnsamblaje>")

                self.posActual=0
                self.meta = "C0"
                self.prioridad=None
                receta.Append("XD")
                return receta
        else:
            file.write("\n\t\t\t\t\t<LineaEnsamblaje NoLinea=\"" + str(self.numero) + "\">\n\t\t\t\t\t\t"+"Brazo " + str(self.numero) + " hace nada\n\t\t\t\t\t</LineaEnsamblaje>")

        return receta