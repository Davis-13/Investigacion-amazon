# Programa de recomendacion musical segun genero.

a = "metal"
b = "disco"
c = "salsa"
d = "reggaeton"

print ("Buenos dias, ingrese su genero musical para que escuche sus musicas favoritas en el playlist")

genero = str (input ("Mi genero musical es: ") )

if genero == a:
    print ("Su playlist recomendado tiene una lista de 50 musicas del genero:",genero)
elif genero == b:
    print ("Su playlist recomendado tiene una lista de 50 musicas del genero:",genero)
elif genero == c:
    print ("Su playlist recomendado tiene una lista de 50 musicas del genero:",genero)
elif genero == d:
    print ("Su playlist recomendado tiene una lista de 50 musicas del genero:",genero)
else :
    print (" No tenemos playlist para el genero ingresado o no fue bien escrito, vuelva a intentarlo")

