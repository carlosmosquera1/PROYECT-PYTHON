# VARIABLES EN PYTHON


my_variable = "Esta es mi variblable"
print(my_variable)  # Imprime el valor de la variable

my_variable_int=5
print(my_variable_int)  # Imprime el valor de la variable entera

my_variable_int_to= str(my_variable_int)
print(my_variable_int_to)  # Convierte el entero a cadena y lo imprime
print(type(my_variable_int_to))  # Imprime el tipo de dato de la variable convertida

my_variable_por=False

print(my_variable_por)  # Imprime el valor de la variable

# concatenacion de variables en print

print(my_variable,my_variable_int_to,my_variable_por)

print(len(my_variable)) # Imprime la longitud de la cadena de texto en my_variable






# variables en una sola linea

# Por buebas practicas no es recomendable, pero se puede hacer

name ,lastname,apodo,AgE= "CARLOS","MOSQUERA","PUCHU",25

print('Hola mi nombre es',name, 'mi apellido es',lastname, 'me dice',apodo, 'y tengo', AgE, 'AÑOS')





# INPUTS

name = input("¿Cuál es tu nombre? ")

lastname = input("¿Cuál es tu apellido? ")

age =int( input("¿Cuál es tu edad? "))

print("Hola", name, lastname, "tienes", age, "años")  # Imprime un saludo con los datos ingresados por el usuario



# Cambiamos su tipo de dato

name = 35
AgE  = 'BRANDON'
print(name)
print(AgE)

# Para forzar el tipo
address: str = 'Mi direccion'
address = True
address = 5.0
address = 1.3
print(type(address))  # Imprime el tipo de dato de la variable address

