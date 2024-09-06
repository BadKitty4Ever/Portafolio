import tkinter as tk

#CREAR UNA VENTANA
#para crea una ventana necesita el metodo tk de tkinter

mi_ventana = tk.Tk()
mi_ventana.title("Jose Aljandro")
mi_ventana.geometry("500x600")

#CREAR UN TEXTO
#para crear un texto, debemos usar el mismo etodo, agregadole ".Label"


etiqueta =  tk.Label(mi_ventana,text="")
etiqueta.pack()

mi_ventana.mainloop()           