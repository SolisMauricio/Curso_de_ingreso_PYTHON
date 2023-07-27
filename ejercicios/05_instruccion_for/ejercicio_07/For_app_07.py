import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        # numero_ingresado = prompt("numero", "numero")
        # numero_ingresado = int(numero_ingresado)

        # for i in range(1, numero_ingresado + 1):
        #     for divisor in range(1, i + 1):
        #         if i % divisor == 0:
        #             print(divisor)
       
        # Definir el rango de números (ejemplo: del 1 al 20)
        '''================================================'''
        '''
        inicio = 1
        fin = 20

        # Utilizar un bucle "for" para iterar sobre cada número en el rango
        for num in range(inicio, fin + 1):
            # Utilizar otro bucle "for" para iterar desde 1 hasta el número mismo
            for divisor in range(1, num + 1):
                # Verificar si el divisor es un divisor del número actual
                if num % divisor == 0:
                    # Si es un divisor, realizar la acción deseada (ejemplo: imprimirlo)
                    print(divisor)
        '''
        '''======================================================'''
        numero_ingresado = prompt("numero", "numero")
        numero_ingresado = int(numero_ingresado)

        
        for i in range(1, numero_ingresado + 1):
            if numero_ingresado % i == 0:
                print(i)
                

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()