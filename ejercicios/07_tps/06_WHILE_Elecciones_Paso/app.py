'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        continuar = True

        maximo_votos = None
        minimo_votos = None

        acumulador_edades = 0
        contador_candidatos = 0
        acumulador_votos = 0

        while continuar == True:
            nombre = prompt("datos", "nombre")
            while nombre is None or not nombre.isalpha():
                nombre = prompt("Error", "ingrese nuevamente su nombre")
            
            edad = prompt("datos", "edad")
            while edad is None or not edad.isdigit or int(edad) < 25:
                edad = prompt("Error", "ingrese nuevamente su edad")
            
            edad = int(edad)
            
            cantidad_votos = prompt("datos", "ingrese cantidad de votos (no menor a ceros)")
            while cantidad_votos is None or not cantidad_votos.isdigit() or int(cantidad_votos) < 0:
                cantidad_votos = prompt("Error", "ingrese nuevamente la cantidad de votos")

            cantidad_votos = int(cantidad_votos)

            # punto A
            if maximo_votos is None or cantidad_votos > maximo_votos:
                maximo_votos = cantidad_votos
                nombre_del_mas_votado = nombre

            #punto B
            if minimo_votos is None or cantidad_votos < minimo_votos:
                minimo_votos = cantidad_votos
                nombre_del_menos_votado = nombre
                edad_del_menos_votado = edad
            
            #punto C
            acumulador_edades += edad
            contador_candidatos += 1

            #punto D
            acumulador_votos += cantidad_votos

            continuar = question(title="quiere continuar")
        
        #punto C
        promedio_edades_candidatos = acumulador_edades /contador_candidatos

        mensaje = f"el candidatos con mas votos es: {nombre_del_mas_votado}\n el nombre del menos votado es: {nombre_del_menos_votado}\n la edad del menos votado es: {edad_del_menos_votado}\n el promedio de edad de los candidatos es: {promedio_edades_candidatos}\n el total de votos emitidos es: {acumulador_votos}"
        print(mensaje)

'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
