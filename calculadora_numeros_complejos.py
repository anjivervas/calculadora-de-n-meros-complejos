def suma(a, b, c, d):
    real = a + c
    imaginario = b + d
    if imaginario < 0: 
        return "la suma es: %d%d i" % (a + c, b + d)
    else:
         return "la suma es: %d+%d i" % (a + c, b + d)

def resta(a, b, c, d):
    real = a - c
    imaginario = b - d
    if imaginario < 0:
        return "la resta es: %d%d i" % (a - c, b - d) 
    else:
        return "la resta es: %d+%d i" % (a - c, b - d) 

def multiplicacion(a, b, c, d): 
    real = a * c
    imaginario = b * d
    if imaginario < 0:
        return "la multiplicacion es: %d%d i" % ((a*c) - (b*d), (b*c) + (a*d) )
    else:
        return "la multiplicacion es: %d+%d i" % ((a*c) - (b*d), (b*c) + (a*d) )

def division(a, b, c, d): 
    if modulo2(c, d) == 0: 
        return "¡¡error: division por cero!!"
    else:
        return "la division es: %d+%d i/%d" % ((a*c) + (b*d), (b*c) - (a*d), modulo2(a, b))

def modulo2(e, f):
    return e ** e + f ** f

def default(): 
    return "la opcion %s no existe en el menu"% case

def switch(case, a, b, c, d): 
    sw={ 
        1: suma(a, b, c, d),
        2: resta(a, b, c, d),
        3: multiplicacion(a, b, c, d),
        4: division(a, b, c, d) 
    } 
    result = sw.get(case)
    if result is None:
        return "¡¡Opción inválida!! Por favor seleccione una opción válida del menú."
    else:
        return result

def menu():
    print("..........CALCULADORA..........")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("...............................")

repetir = True 
while repetir:
    print("**********CALCULADORA DE NÚMEROS COMPLEJOS**********") 
    print("Números de la forma a+bi")
    print("Parte REAL: a, parte IMAGINARIA: b")
    menu()
    case = int(input("Seleccione una operación "))
    a = int(input("Escriba la parte real del primer numero complejo "))
    b = int(input("Escriba la parte imaginaria del primer numero complejo "))
    print("Número ingresado %d+%d i" %(a, b)) 
    c = int(input("Escriba la parte real del segundo numero complejo "))
    d = int(input("Escriba la parte imaginaria del segundo numero complejo "))
    print("Número ingresado %d+%d i" % (c, d))
    print(switch(case, a, b, c, d))
    rep = input("¿Desea realizar otra operación? [S/N] ") 
    if rep.upper() == "S":
        repetir = True
    else:
        repetir = False