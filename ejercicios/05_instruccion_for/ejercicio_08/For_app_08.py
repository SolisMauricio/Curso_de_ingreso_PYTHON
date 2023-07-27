import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        numero_primo = prompt("numero", "numero")
        while not numero_primo.isdigit():
            numero_primo = prompt("numero", "numero")
        numero_primo = int(numero_primo)
        
        if numero_primo > 1:
            for divisor in range(2, numero_primo):
                if numero_primo % divisor == 0:
                    print(f"el numero {numero_primo} no es primo")
                    break
                else:
                    print(f"el numero {numero_primo} es primo")
                    break
        else: 
            print(f"el numero {numero_primo} no es primo")
                    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()