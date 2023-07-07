import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_04
---
Enunciado:
<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_04/app.py
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt
 y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
=======
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt 
y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
>>>>>>> 1f442cc264dd3330454d5b18f58c36600d1c9652:ejercicios/01_entrada_salida/ejercicio_04/app_ES_04.py
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre_ingresado = prompt('nombre' , 'ingrese su nombre')
        
        self.txt_nombre.delete(0, 100)

        self.txt_nombre.insert( 0,nombre_ingresado)

        #alert(nombre_ingresado)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()