        '''OBTENER NUMERO MAXIMO Y MINIMO'''
        numero_maximo = None
        numero_minimo = None
        
        while True:
            numero_ingresado = prompt("numeros", "ingrese numeros")

            if numero_ingresado == None:
                break
            elif numero_ingresado.isalpha():
                alert(title="error", message="no ingreso un numero")
                continue 
        
            if numero_maximo is None or numero_ingresado > numero_maximo: 
                numero_maximo = numero_ingresado
            elif numero_minimo is None or numero_ingresado < numero_minimo:
                numero_minimo = numero_ingresado
        
        ''' ====================================================================================== '''