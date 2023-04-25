from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

#Entrada
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, pandx = 5, pandy = 5)

#Botones
boton1 = Button(ventana, text = "1", width = 5, height = 2)
boton2 = Button(ventana, text = "2", width = 5, height = 2)
boton3 = Button(ventana, text = "3", width = 5, height = 2)
boton4 = Button(ventana, text = "4", width = 5, height = 2)
boton5 = Button(ventana, text = "5", width = 5, height = 2)
boton6 = Button(ventana, text = "6", width = 5, height = 2)
boton7 = Button(ventana, text = "7", width = 5, height = 2)
boton8 = Button(ventana, text = "8", width = 5, height = 2)
boton9 = Button(ventana, text = "9", width = 5, height = 2)
boton0 = Button(ventana, text = "0", width = 13, height = 2)

boton_borrar = Button(ventana, text = "AC", width = 5, height = 2)
boton_parenthesis1 = Button(ventana, text = "(", width = 5, height = 2)
boton_parenthesis2 = Button(ventana, text = ")", width = 5, height = 2)
boton_punto = Button(ventana, text = ".", width = 5, height = 2)

boton_div = Button(ventana, text = "/", width = 5, height = 2)
boton_mult = Button(ventana, text = "x", width = 5, height = 2)
boton_sum = Button(ventana, text = "+", width = 5, height = 2)
boton_rest = Button(ventana, text = "-", width = 5, height = 2)
boton_igual = Button(ventana, text = "=", width = 5, height = 2)

# interfaz

ventana.mainloop()