### SETS ###

my_set = set()  # Crea un conjunto vacío.
my_other_set ={}


print(type(my_other_set))  # Imprime el tipo de dato de my_other_set, que es un diccionario.
print(type(my_set))  # Imprime el tipo de dato de my_set.

my_other_set = {25, 'CARLOS', 'MOSQUERA', 1.75}  # Crea un conjunto con elementos.

print(type(my_other_set))  #  Imprime el contenido de my_other_set.

print(len(my_other_set))  # Imprime la longitud del conjunto my_other_set.

my_other_set.add('PUCHU')  # Agrega un nuevo elemento al conjunto my_other_set.

print(my_other_set)  # Imprime my_other_set después de agregar el nuevo elemento. // UN SET NO ES UNA ESTRUCTURA ORDENADA

print('carlos' in my_other_set)  # Verifica si 'carlo' está en my_other_set (debería ser False).
print('CARLOS' in my_other_set)  # Verifica si 'CARLOS' está en my_other_set (debería ser True).

my_other_set.remove('PUCHU')  # Elimina 'PUCHU' del conjunto my_other_set.
print(my_other_set)  # Imprime my_other_set después de eliminar 'PUCHU.

my_other_set.clear() # Limpia todos los elementos del conjunto my_other_set.

print(len(my_other_set))  # Imprime my_other_set después de limpiar todos sus elementos.

del my_other_set  # Elimina el conjunto my_other_set.
# print(my_other_set)  # Intenta imprimir my_other_set después de eliminarlo (esto generará un error).
print()
my_set = {'CARLOS',25,'MARIO','MOSQUERA'}  # Crea un conjunto con números.
my_list= list(my_set)  # Convierte el conjunto my_set en una lista.
print(my_list)  # Imprime la lista resultante de la conversión.
print(my_list[0])

my_other_set = {'JAVA','ASSEMBLER','SQL','PYTHOM'}

my_new_set = my_set.union(my_other_set)  # Une my_set y my_other_set en un nuevo conjunto.D

#print(my_new_set.union(my_new_set).union(my_set).union('JAVASCRIPT','DJANGO'))  # Imprime el nuevo conjunto resultante de la unión.

print(my_new_set)  # Imprime el nuevo conjunto resultante de la unión.