### TUPLAS ###

my_tuple = tuple()  # Crea una tupla vacía.
my_other_tuple = (25, 'CARLOS', 'MOSQUERA', 1.75)  # Crea una tupla con elementos.

my_tuple = (25,1.75,'CARLOS','MARIO','MOSQUERA','CARLOS','PUCHU','CARLOS')  # Inicializa my_tuple como una tupla con elementos.
print(type(my_tuple))  # Imprime el tipo de dato de my_tuple.
print(my_tuple)  # Imprime el contenido de my_tuple.

print(my_tuple[0])  # Imprime el primer elemento de la tupla.
print(my_tuple[-1])  # Imprime el ultimo elemento de la tupla.

print(my_tuple.count('CARLOS'))  # Cuenta cuántas veces aparece 'PUCHU' en la tupla (debería ser 0).
print(my_tuple.index('MARIO'))  # Busca el índice del primer elemento 'mario' en la tupla (debería ser 3).


my_suma_tupla = my_tuple + my_other_tuple  # Suma dos tuplas.
print(my_suma_tupla)  # Imprime el resultado de la suma de las tuplas.
print(my_suma_tupla* 2)  # Imprime la tupla duplicada (repetida dos veces).
print()
print(my_suma_tupla[0:7])  # Imprime una porción de la tupla (del índice 0 al 2).
#  my_other_tuple['carlos']='mosquera'  # Intenta asignar un valor a un índice de la tupla (esto generará un error, ya que las tuplas son inmutables).