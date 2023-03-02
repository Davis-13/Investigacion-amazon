# Programa que suma el costo de todos productos comprados.

# Variable
cantprod = 0
sum = 0
sumatotal = 0
comprar = 0


print ("Le damos la bienvenida a Amazon")

comprar = int (input ("Desea hacer una compra ingrese 1, sino desea hacer compra ingrese la opcion 2: ") )

if comprar == 1 :
    cantprod = int (input ("Ingrese la cantidad de productos a comprar: ") )
    for i in range(cantprod):
        sum = float ( input("Ingrese el costo del producto comprado: "))
        sumatotal = sumatotal + sum
    print ("La suma total de su compra es: ", sumatotal)
elif comprar == 2:
    print ("A vuelto a la ventana principal de amazon")
else :
    print ("La opcion ingresada no es correcta, vuelva a intentarlo")
