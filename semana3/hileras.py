# Tema Hileras

message = input("Digite lo que quiera: ")

print(message)

# len() encontrar la cantidad de caracteres que tiene una hilera

print(len(message))

# Indices

print(message[0])
print(message[-3])

# Concatenacion de hileras

hilera1 = "Hilera inicial"

# Concatenacion simple
print(hilera1 + " mas otra hilera")
print(hilera1)

# Concatenacion modificando la variable

hilera1 +=  " esta hilera si modifico la inicial"
print(hilera1)

# Inyectando texto

hilera2 = "Hola {} {}! como estas?".format(message, "Raygada")
#hilera2.format("Jose")
print(hilera2)
print(hilera2[3:6])
print(hilera2[:6])
print(hilera2[3:])
print(hilera2[::-1])

