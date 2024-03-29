import random  
 
error = True
numero = random.randint(-5, 5)
 
try:
    if numero < 0:
        raise TypeError("No se puede calcular la raiz")
    print("numero %.2f y su raíz cuadrada %.2f" % (numero, numero ** 0.5))
except (TypeError) as mensaje:
    print("Ocurrió una excepción identificada.", mensaje)
else:
    print("No hubo errorres.")
    error = False
finally:
    if error:
        print("Se ha dado un error.")
    else:
        print("¡Se ha podido encontrar un resultado!")
