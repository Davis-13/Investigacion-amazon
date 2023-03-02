#Busqueda de audifonos en amazon

# variable

tipo = 0
tipo1 = 0
tipo2 = 0

print ("Bienvenido a amazon, la tienda mas grande de compra en linea")

print ("Ingrese los siguientes datos para brindarle un producto acorde a sus necesidades")

tipo = int (input ("Ingrese tipo de audifonos que desea 1-alambrico, 2-inalambrico: "))
tipo1 = int (input ("Opcion 1-trabajo, 2-deportivo: "))
tipo2 = int (input ("Opcion 1- hasta 50$, 2-mas de 50$: "))

if tipo == 1 :
    if tipo1 == 1 :
        if tipo2 == 1 :
            print ("El siguiente producto es un audifono alambrico, de trabajo y con costo por debajo de 50$")
        elif tipo2 == 2 :
            print ("El siguiente producto es un audifono alambrico, de trabajo y con costo por encima de 50$")
        else :
            print ("La opcion ingresada no es correcta, vuelva ingresar los datos")
    elif tipo1 == 2 :
        if tipo2 == 1 :
            print ("El siguiente producto es un audifono alambrico, deportivo y con costo por debajo de 50$")
        elif tipo2 == 2 :
            print ("El siguiente producto es un audifono alambrico, deportivo y con costo por encima de 50$")
        else :
            print ("La opcion ingresada no es correcta, vuelva ingresar los datos")
    else :
            print ("La opcion ingresada no es correcta, vuelva ingresar los datos")
elif tipo == 2 :
    if tipo1 == 1 :
        if tipo2 == 1 :
            print ("El siguiente producto es un audifono inalambrico, de trabajo y con costo por debajo de 50$")
        elif tipo2 == 2 :
            print ("El siguiente producto es un audifono inalambrico, de trabajo y con costo por encima de 50$")
        else :
            print ("La opcion ingresada no es correcta, vuelva ingresar los datos")
    elif tipo1 == 2 :
        if tipo2 == 1 :
            print ("El siguiente producto es un audifono inalambrico, deportivo y con costo por debajo de 50$")
        elif tipo2 == 2 :
            print ("El siguiente producto es un audifono inalambrico, deportivo y con costo por encima de 50$")
        else :
            print ("La opcion ingresada no es correcta, vuelva ingresar los datos")
    else :
        print ("La opcion ingresada no es correcta, vuelva ingresar los datos")
else :
    print ("La opcion ingresada no es correcta, vuelva ingresar los datos")

#fin