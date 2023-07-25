import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0

        contador_negativos = 0 
        contador_positivos = 0
        contador_ceros = 0
        while True:
            numeros_ingresados = prompt("numeros", "ingrese numeros")

            if numeros_ingresados == None:
                break
            elif numeros_ingresados.isalpha():
                continue
            
            numeros_ingresados = int(numeros_ingresados)
            if numeros_ingresados > 0:
                    contador_positivos += 1
                    acumulador_positivos += numeros_ingresados
            elif numeros_ingresados < 0:
                    contador_negativos += 1
                    acumulador_negativos += numeros_ingresados
            else:
                    contador_ceros += 1

        diferencia_positivos_y_negativos = contador_positivos - contador_negativos

        mensaje = f"la suma de los negativos es: {acumulador_negativos}\n"
        mensaje += f"la cantidad de numeros negativos es: {contador_negativos}\n"
        mensaje += f"la suma de los positivos es: {acumulador_positivos}\n"
        mensaje += f"la cantidad de numeros positivos es: {contador_positivos}\n"
        mensaje += f"la cantidad de ceros es: {contador_ceros}\n"
        mensaje += f"la diferencia entre positivos y negativos es: {diferencia_positivos_y_negativos}"

        alert(title="numeros", message=mensaje)    
                       

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
