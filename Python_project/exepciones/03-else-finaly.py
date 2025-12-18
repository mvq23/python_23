try:
    n1 = int(input("Ingrese primer numero: "))
except Exception as e:
    print ("Ocurrio un error")
else:
   print("No hubo error")
finally:
    print("Ejecucion siempre")