# Programa de inteligente con Alexa

#Varibles

luces = 1
aa = 2
lucesala = 1
lucehab = 2
lucebaño = 3
aasala = 1
aahab = 2


opc1 = 0
opc2 = 0




print ("Hola Soy Alexa, estoy a sus ordenes")

print ("Desea encender las luces y el A/A")

opc1 = int (input ("Tome la opcion 1-Luces o 2- A/A: ") )
#opc2 = int (input ("Elija la opcion 1-Luces de sala, 2-Luces de Habitacion y 3-Luces de Baño: "))
#opc3 = int (input ("Elija la opcion 1-A/A de la sala, 2-A/A de la Habitacion: ") )

if opc1 == luces:
    opc2 = int (input ("Elija la opcion 1-Luces de sala, 2-Luces de Habitacion y 3-Luces de Baño: "))
    if opc2 == lucesala :
        print ("Las luces de la sala fueron encendidas")

    elif opc2 == lucehab :
        print ("Las Luces de las Habitaciones fueron encendidas")

    elif opc2 == lucebaño :
        print ("Las Luces del baño fueron encendidas")

    else :
        print ("Esa opcion de luces no existe, vuelva a intentarlo")

elif opc1 == aa:
    opc3 = int (input ("Elija la opcion 1-A/A de la sala, 2-A/A de la Habitacion: ") )
    if opc3 == aasala :
        print ("Las luces de la sala fueron encendidas")

    elif opc3 == aahab :
        print ("Las Luces de las Habitaciones fueron encendidas")
    else :
        print ("Esa opcion de a/a no existe, vuelva a intentarlo")

else :
    print ("La opcion ingresada no es correcta, vuelva a intentarlo")



