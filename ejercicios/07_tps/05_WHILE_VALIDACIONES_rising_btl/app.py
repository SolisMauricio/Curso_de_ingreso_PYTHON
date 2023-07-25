import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        apellido = prompt("datos", "apellido")
        while apellido is None or not apellido.isalpha():
            apellido = prompt("error", "ingrese un apellido valido")
        
        edad = prompt("datos", "edad")
        while edad is None or not edad.isdigit() or (int(edad) < 18 or int(edad) > 90):
            edad = prompt("error", "ingrese una edad valida")
            
        estado_civil = prompt("datos", "estado civil [Casado/Casada, Soltero/Soltera, Divorciado/Divorciada, Viudo/ Viuda]")
        while estado_civil != "Casado" and estado_civil !="Casada" and estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Divorsiado" and estado_civil != "Divorciada" and estado_civil != "Viudo" and estado_civil != "Viuda":
            estado_civil = prompt("error", "ingrse un estado civil correcto")

        match estado_civil:
            case "soltero" | "soltera":
                estado_civil= "soltero/a"
            case "Casado" | "casada":
                estado_civil= "casado/a"
            case "divorsiado" | "divorciada":
                estado_civil = "divorsiado/a"
            case _:
                estado_civil = "viudo/a"
        
        legajo = prompt("datos", "ingrese su nemero de legajo")
        while legajo is None or not legajo.isdigit() or int(legajo) < 999:
            legajo = prompt("error", "ingrese un numero de legajo valido")

        self.txt_apellido.delete(0, tkinter.END)
        self.txt_apellido.insert(0, apellido)

        self.txt_edad.delete(0, tkinter.END)
        self.txt_edad.insert(0, edad)

        #self.combobox_tipo.delete(0, 100)
        self.combobox_tipo.set(estado_civil)

        self.txt_legajo.delete(0, tkinter.END)
        self.txt_legajo.insert(0, legajo)

        

        
            

















if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
