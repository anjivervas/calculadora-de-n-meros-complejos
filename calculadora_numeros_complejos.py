from funciones import *

def default(): #crear un menu para trabajar con un switch
    return "la opcion %s no existe en el menu"% case

def switch(case, a, b, c, d): #simulacion del switch
    sw={ #defino variables y creo una lista
        1: suma(a, b, c, d),
        2: resta(a, b, c, d),
        3: multiplicacion(a, b, c, d),
        4: division(a, b, c, d) #especificacion de argumentos
    } 
    result = sw.get(case)
    if result is None:
        return "¡¡Opción inválida!! Por favor seleccione una opción válida del menú."
    else:
        return result

def menu(): #menu para el usuario
    print("..........CALCULADORA..........")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División") 
    print("...............................")

repetir = True #defino una variable booleana
while repetir:
    print("**********CALCULADORA DE NÚMEROS COMPLEJOS**********") #defino el menu principal donde empieza el programa
    print("Números de la forma a+bi")
    print("Parte REAL: a, parte IMAGINARIA: b")
    menu()
    case = int(input("Seleccione una operación ")) #definicion del case por parte del usuario (suma, resta, multiplicacion o division)
    a = int(input("Escriba la parte real del primer numero complejo ")) #escribir el primer numero de la escuacion que desea calcular (parte real)
    b = int(input("Escriba la parte imaginaria del primer numero complejo ")) #escribir el primer numero de la escuacion que desea calcular (parte imaginaria)
    print("Número ingresado %d+%d i" %(a, b)) #descripcion para el usuario (decirle que numero ingreso)
    c = int(input("Escriba la parte real del segundo numero complejo ")) #escribir el segundo numero de la escuacion que desea calcular (parte real)
    d = int(input("Escriba la parte imaginaria del segundo numero complejo ")) #escribir el segundo numero de la escuacion que desea calcular (parte imaginaria)
    print("Número ingresado %d+%d i" % (c, d)) #descripcion para el usuario (decirle que numero ingreso)
    
    res = switch(case,a,b,c,d)
    
    print(res)

    rep = input("¿Desea realizar otra operación? [S/N] ") #opciones para seguir con el calculo
    if rep.upper() == "S":
        repetir = True
    else:
        repetir = False