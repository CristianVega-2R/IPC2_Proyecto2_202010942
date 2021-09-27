import tkinter
def funcionPrueba(event):
    global var
    print(var.get())

ventana = tkinter.Tk()
ventana.geometry("500x500")

lista = ['1','2','3']
var=tkinter.StringVar(ventana)
var.set('Seleccionar')
seleccion = tkinter.OptionMenu(ventana,var,*lista, command=funcionPrueba)
seleccion.pack()

ventana.mainloop()

