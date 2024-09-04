# Crear una cadena de texto de tipo str que contenga una oración completa.
Cadena = "Mi nombre es Fernando Huerta Ramos "

# Convertir la cadena a mayúsculas y minúsculas.
print (Cadena.lower())
print (Cadena.upper())

# Crear una lista de palabras a partir de la cadena original.
print (Cadena.split())

# Contar el número de veces que aparece una letra específica en la cadena
print ("El numero de veces que sale la letra (e) son ",Cadena.count('e'),"Veces")

#Verificar si la cadena comienza y termina con palabras específicas.
print ("Verifica si la cadena comienza con la letra (a) ",Cadena.startswith('e'))
print ("Verifica si la cadena termina con la letra (a)",Cadena.endswith('e'))

# Reemplazar todas las apariciones de una palabra en la cadena con otra.
print (Cadena.replace("Fernando","Mario"))

# Concatenar la cadena original con otra cadena proporcionada por el usuario.
Cadena2 = " Estudio en la Universidad de Guadalajara"
print (Cadena + Cadena2)

# Dividir la cadena en una lista de palabras y luego unirla en una nueva cadena separada por guiones.
Dividir = Cadena.split()
print (Cadena = "_".join(Dividir)
