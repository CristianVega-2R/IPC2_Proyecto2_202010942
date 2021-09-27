import tkinter


ventana = tkinter.Tk()

ventana.geometry("400x300")
cajaTexto =tkinter.Entry(ventana)
cajaTexto.pack()
cajaTexto.place(x=10,y=10)

def texto():
    print(cajaTexto.get())

boton = tkinter.Button(ventana, text="clickeame", command=texto)
boton.pack()

ventana.mainloop()