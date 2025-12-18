try:
    n1 = int(input("Ingrese primer numero: "))
#except Exception as e:
#    print (type(e))
    test_error
except ValueError as e:
    print ("Error ingrese un valor correcto:", e)  
except NameError as e:
    print ("Ocurrio un error:", e) 