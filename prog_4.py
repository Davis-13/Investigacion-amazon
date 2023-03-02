#Apertura de cuenta de amazon

print ("Bienvenido a Amazon, antes de iniciar su compra es necesario ingrese sus datos personales para abrir una cuenta")

#declaracion de variable
M = "masculino"
F = "femenino"
validacion = 0
año_actual = 0
año_nac = 0
edad = 0

print ("Ingrese su nombre completo: ")
nombre = str (input ())
print ("Ingrese su genero en letra masculino o femenino: ")
genero = str (input ())
print ("Ingrese su correo electronico: ")
correo = str (input ())

año_nac = int (input ("Ingrese su año de nacimiento: "))
año_actual = int (input ("Ingrese el año actual:"))

edad = año_actual - año_nac

if edad >= 18 :
        print ("Es usted una persona con mayoria de edad para abrir una cuenta en amazon, confirmar si sus datos son correctos ")
        print ("Su nombre es:", nombre)
        print ("Su genero es:", genero)
        print ("Su correo electronico es:", correo)
else :
    ("Pida a sus padres le ayuden a crear una cuenta en amazon para que pueda realizar sus compras")
    
