from Brazo import Brazo
import tkinter
from tkinter import ttk, HORIZONTAL
from Productos import Producto
import xml.etree.ElementTree as ET
from Linea import Linea
from ListaEnlazada import ListaEnlazada
import time
import os

raiz=0
raiz2=0
listaPedidos=ListaEnlazada()
listaLineas = ListaEnlazada()
listaProductos = ListaEnlazada()
listaProductosEstaticos = ListaEnlazada()
listaProductosAux = ListaEnlazada()
listaProductosHTML = ListaEnlazada()
listaProductosEstaticosHTML = ListaEnlazada()
listaProductosAuxHTML = ListaEnlazada()
listaProductosXML = ListaEnlazada()
listaProductosEstaticosXML = ListaEnlazada()
listaProductosAuxXML = ListaEnlazada()
nombreSimulación=""
cantLineas=0

#PEDIR_PRODUCTOS
def recogerProductos(ruta):
    """Datos del XML"""
    arbol = ET.parse(ruta)
    global raiz2
    raiz2 = arbol.getroot()


var=""
def configurarProductos():
    recogerProductos(cajaTextoPedidos.get())

    global nombreSimulación
    for productos in raiz2.iter("Nombre"):
        nombreSimulación=productos.text

    global listaPedidos
    for productos in raiz2.iter("ListadoProductos"):
        for listado in productos.iter("Producto"):
            listaPedidos.Append(listado.text.replace("\n", "").replace("\t",""))
    global var
    var=tkinter.StringVar(ventana)
    var.set('Seleccionar')
    listaAuxiliar = []
    for i in range(len(listaPedidos)):
        listaAuxiliar.append(listaPedidos.Seleccionar(i))
    global seleccion
    seleccion = tkinter.OptionMenu(ventana, var, *listaAuxiliar, command=buscarProducto)
    seleccion.pack()
    seleccion.place(x=30, y=300)
    seleccion.config(width=10)

#MAQUINA


def recoger(ruta):
    """Datos del XML"""
    print(ruta)
    arbol = ET.parse(ruta)
    global raiz
    raiz = arbol.getroot()


def configurar():
    recoger(str(cajaTextoMaquina.get()))
    for lineas in raiz.iter("CantidadLineasProduccion"):
        global cantLineas
        cantLineas=int(lineas.text)

    """Leyendo la configuración de la máquina"""
    for listado in raiz.iter("ListadoLineasProduccion"):
        """Accediendo a una por una"""
        for linea in listado:
            """Número de línea"""
            for numero in linea.iter("Numero"):
                numeroObjeto=(int(numero.text))
            for numero in linea.iter("CantidadComponentes"):
                componentes=(int(numero.text))
            for numero in linea.iter("TiempoEnsamblaje"):
                tiempo=(int(numero.text))
            listaLineas.Append(Linea(numeroObjeto, componentes, tiempo))


    """Leyendo los productos de la maquina"""
    for listadoProductos in raiz.iter("ListadoProductos"):
        """Accediendo a cada producto"""
        for producto in listadoProductos:
            for nombre in producto.iter("nombre"):
                nombreObjeto = nombre.text
                nombreObjeto=nombreObjeto.replace("\n","").replace("\t","")
            for elaboracion in producto.iter("elaboracion"):
                elaboracionObjeto = elaboracion.text
                elaboracionObjeto=((((elaboracionObjeto.replace(" ", "")).replace("\n",""))).replace("\t","").split("p"))
                listaProductos.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosEstaticos.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosAux.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosHTML.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosEstaticosHTML.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosAuxHTML.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosXML.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosEstaticosXML.Append(Producto(nombreObjeto, elaboracionObjeto))
                listaProductosAuxXML.Append(Producto(nombreObjeto, elaboracionObjeto))

brazos = ListaEnlazada()
#ALGORITMO
def crear():
    for i in range(cantLineas):
        brazos.Append("Linea "+str(i+1))

def crearHtml():
    listaBrazos = ListaEnlazada()
    file = open("pagina.html", "w")
    file.write("""<!DOCTYPE html>
<head>
</head>
<body>\n""")
    """Crear brazos"""
    for i in range(len(listaLineas)):
        listaBrazos.Append(Brazo(int(listaLineas.SeleccionarValor(i).getNumero()),
                                 int(listaLineas.SeleccionarValor(i).getComponentes()),
                                 int(listaLineas.SeleccionarValor(i).getTiempo())))
    """Trabajar productos"""
    for i in range(len(listaProductosHTML)):
        file.write("""<table>
<h1>""" + str(listaProductosHTML.Seleccionar(i).getNombre()) + """</h1>""")
        """Ver la receta del pedido"""
        cola = listaProductosEstaticosHTML.SeleccionarValor(i).getReceta()
        recetaActual = listaProductosHTML.Seleccionar(i).getReceta()
        recetaAux = listaProductosAuxHTML.Seleccionar(i).getReceta()
        """Ver brazos a accionar y delimitar meta de cada uno"""
        """Encontrar el componente y luego eliminarlo, luego buscar otra vez iterativamente hasta terminar"""
        while (len(recetaActual) != 0):
            for l in range(cantLineas):
                for k in range(0, len(recetaActual), 2):
                    if "L" + str(l + 1) == str(recetaActual.Seleccionar(k)):
                        listaBrazos.Modificar(listaBrazos.Seleccionar(l).asignarMeta(recetaActual.Seleccionar(k + 1)),
                                              l)
                        recetaActual.Remove(k)
                        recetaActual.Remove(k)
                        recetaAux.Remove(k)
                        recetaAux.Remove(k)
                        break
            """Trabajar con los brazos actuales"""
            prioridad = 0
            contadorSegs = 0

            while int(len(cola) / 2) != int(prioridad / 2):
                print("Segundo " + str(contadorSegs + 1))
                longitud = len(recetaActual)
                file.write("\n<tr>\n")
                for k in range(len(listaBrazos)):
                    recetaActual = listaBrazos.SeleccionarValor(k).ticHTML(recetaActual, prioridad, cola, file,
                                                                           contadorSegs)
                file.write("\n</tr>")
                if longitud - 2 == len(recetaActual):
                    prioridad += 2
                elif longitud + 1 == len(recetaActual):
                    prioridad += 2
                    recetaActual.Remove(len(recetaActual) - 1)
                contadorSegs += 1
                global texto
                global conteo
                texto.set(str(contadorSegs))
            listaProductosEstaticosHTML.SeleccionarValor(i).reset
            listaProductosHTML.SeleccionarValor(i).reset
            listaProductosAuxHTML.SeleccionarValor(i).reset
    file.write("\n</table>")
    file.write("\n</body>\n")
    file.write("</html>")
    file.close()

def crearXml():
    datos=""
    listaBrazos = ListaEnlazada()
    file = open("documento.xml", "w")
    file.write("""<SalidaSimulación>\n""")
    """Crear brazos"""
    for i in range(len(listaLineas)):
        listaBrazos.Append(Brazo(int(listaLineas.SeleccionarValor(i).getNumero()),
                                 int(listaLineas.SeleccionarValor(i).getComponentes()),
                                 int(listaLineas.SeleccionarValor(i).getTiempo())))

    global nombreSimulación
    file.write("""\t<Nombre>\t\t""" + str(nombreSimulación) + """\t</Nombre>\n\t<ListaProductos>""")
    """Trabajar productos"""
    for i in range(len(listaProductosXML)):
        for j in range(len(listaPedidos)):
            if str(listaProductosXML.Seleccionar(i).getNombre()) == str(listaPedidos.Seleccionar(j)):
                file.write("\n\t\t<Producto>\n")
                file.write("\t\t\t<Nombre>\n\t\t\t\t" + str(listaPedidos.SeleccionarValor(
                    j)) + "\n\t\t\t</Nombre>\n\t\t\t<TiempoTotal> CANTIDAD SEGUNDOS </TiempoTotal>\n\t\t\t<ElaboracionOptima>")
                """Ver la receta del pedido"""
                cola = listaProductosEstaticosXML.SeleccionarValor(i).getReceta()
                recetaActual = listaProductosXML.Seleccionar(i).getReceta()
                recetaAux = listaProductosAuxXML.Seleccionar(i).getReceta()
                """Ver brazos a accionar y delimitar meta de cada uno"""
                """Encontrar el componente y luego eliminarlo, luego buscar otra vez iterativamente hasta terminar"""
                while (len(recetaActual) != 0):
                    for l in range(cantLineas):
                        for k in range(0, len(recetaActual), 2):
                            if "L" + str(l + 1) == str(recetaActual.Seleccionar(k)):
                                listaBrazos.Modificar(
                                    listaBrazos.Seleccionar(l).asignarMeta(recetaActual.Seleccionar(k + 1)),
                                    l)
                                recetaActual.Remove(k)
                                recetaActual.Remove(k)
                                recetaAux.Remove(k)
                                recetaAux.Remove(k)
                                break
                    """Trabajar con los brazos actuales"""
                    prioridad = 0
                    contadorSegs = 0
                    while int(len(cola) / 2) != int(prioridad / 2):
                        print("Segundo " + str(contadorSegs + 1))
                        longitud = len(recetaActual)
                        file.write("\n\t\t\t\t<Tiempo NoSegundo=\"" + str(contadorSegs) + "\">\n")
                        for k in range(len(listaBrazos)):
                            recetaActual = listaBrazos.SeleccionarValor(k).ticXML(recetaActual, prioridad, cola, file)
                        file.write("\n\t\t\t\t</Tiempo>")
                        if longitud - 2 == len(recetaActual):
                            prioridad += 2
                        elif longitud + 1 == len(recetaActual):
                            prioridad += 2
                            recetaActual.Remove(len(recetaActual) - 1)
                        contadorSegs += 1
                        global texto
                        global conteo
                        texto.set(str(contadorSegs))
                    listaProductosEstaticosXML.SeleccionarValor(i).reset
                    listaProductosXML.SeleccionarValor(i).reset
                    listaProductosAuxXML.SeleccionarValor(i).reset
                    file.write("\n\t\t\t</ElaboracionOptima>\n")
                    file.write("\n\t\t</Producto>\n")
    file.write("\n</ListadoProductos>")
    file.write("\n</SalidaSimulacion>\n")
    file.close()#terminar de escribir

"""Se debe pasar una lista con los productos"""
def buscarProducto(event):
    crearTabla()
    global tabla

    listaBrazos = ListaEnlazada()

    """Crear brazos"""
    for i in range(len(listaLineas)):
        listaBrazos.Append(Brazo(int(listaLineas.SeleccionarValor(i).getNumero()), int(listaLineas.SeleccionarValor(i).getComponentes()),int(listaLineas.SeleccionarValor(i).getTiempo())))
    """Trabajar productos"""

    for i in range(len(listaProductos)):
        global var
        if str(listaProductos.Seleccionar(i).getNombre()) == str(var.get()):
            tabla.insert("", 0, text="Iniciada elaboracion de " + var.get(), values=0)
            """Ver la receta del pedido"""
            cola = listaProductosEstaticos.SeleccionarValor(i).getReceta()
            recetaActual = listaProductos.Seleccionar(i).getReceta()
            recetaAux = listaProductosAux.Seleccionar(i).getReceta()
            """Ver brazos a accionar y delimitar meta de cada uno"""
            """Encontrar el componente y luego eliminarlo, luego buscar otra vez iterativamente hasta terminar"""
            while (len(recetaActual) != 0):
                for l in range(cantLineas):
                    for k in range(0, len(recetaActual), 2):
                        if "L" + str(l + 1) == str(recetaActual.Seleccionar(k)):
                            listaBrazos.Modificar(
                                listaBrazos.Seleccionar(l).asignarMeta(recetaActual.Seleccionar(k + 1)), l)
                            recetaActual.Remove(k)
                            recetaActual.Remove(k)
                            recetaAux.Remove(k)
                            recetaAux.Remove(k)
                            break
                """Trabajar con los brazos actuales"""
                prioridad = 0
                contadorSegs = 0
                progressbar = len(recetaActual)
                while int(len(cola) / 2) != int(prioridad / 2):
                    longitud = len(recetaActual)
                    for k in range(len(listaBrazos)):
                        recetaActual = listaBrazos.SeleccionarValor(k).tic(recetaActual, prioridad, cola, tabla,
                                                                           contadorSegs)
                    if longitud - 2 == len(recetaActual):
                        prioridad += 2
                    elif longitud + 1 == len(recetaActual):
                        prioridad += 2
                        recetaActual.Remove(len(recetaActual) - 1)
                    contadorSegs += 1
                    global texto
                    global conteo
                    texto.set(str(contadorSegs))

                    global pb1
                    pb1['value'] = ((-len(recetaActual)+progressbar)/progressbar)*100
                    time.sleep(1)
                    ventana.update_idletasks()

                tabla.insert("", 0, text="El " + str(var.get()) + " se ensambló de manera óptima en " + str(
                    contadorSegs) + " segundos", values=str(contadorSegs))

                listaProductosEstaticos.SeleccionarValor(i).reset
                listaProductos.SeleccionarValor(i).reset
                listaProductosAux.SeleccionarValor(i).reset


ventana = tkinter.Tk()
ventana.geometry("1000x600")

botonMaquina = tkinter.Button(ventana, text="maquina", command=configurar)
botonMaquina.pack()
botonMaquina.place(x=200,y=150)

cajaTextoMaquina = tkinter.Entry(ventana)
cajaTextoMaquina.pack()
cajaTextoMaquina.place(x=30, y=150)

botonPedidos = tkinter.Button(ventana, text="pedidos", command=configurarProductos)
botonPedidos.pack()
botonPedidos.place(x=200,y=50)

cajaTextoPedidos = tkinter.Entry(ventana)
cajaTextoPedidos.pack()
cajaTextoPedidos.place(x=30,y=50)

botonHTML = tkinter.Button(ventana, text="html", command=crearHtml)
botonHTML.pack()
botonHTML.place(x=200, y=200)
botonXML = tkinter.Button(ventana, text="xml", command=crearXml)
botonXML.pack()
botonXML.place(x=200, y=250)


conteo = tkinter.Label(ventana, text="")
texto = tkinter.StringVar()
texto.set("")
conteo.config(textvariable=texto)
conteo.pack()
conteo.place(x=800,y=800)


pb1 = ttk.Progressbar(ventana, orient=HORIZONTAL, length=100)
pb1.pack(expand=True)
pb1.place(x=500,y=500)

tabla = ttk.Treeview(ventana, columns=("#1"))

info = tkinter.Label(ventana, text="Cristian Raúl Vega Rodríguez\n202010942\nIntroducción a la Programación y Computación Sección \"A\"\nIngeniería en Sistemas\n4to. Semestre")
info.pack()
info.place(x=50,y=500)
seleccion = tkinter.OptionMenu(ventana, None, None)

def crearTabla():
    crear()
    tabla.pack()
    tabla.place(x=400,y=10)
    tabla.column("#0",width=400)
    tabla.heading("#0", text=("Proceso"))
    tabla.heading("#1", text=("Segundo"))


ventana.mainloop()