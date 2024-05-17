def suma(a, b, c, d):
    """Sumary: Suma de numeros complejos

    Args:
        a (int): parte real
        b (int): parte imaginaria
        c (int)
        d (int)
    
    Returns:
        int: suma
    """
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