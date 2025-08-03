open_list = list() # Crea una lista vacía.
list_1=['CAMILA','CATERIN','FAMILIA','CASA',25,'CARRO',21,22,'PAPA','MAMA'] # Crea una lista con varios tipos de datos.
print(type(open_list)) # Imprime el tipo de dato de open_list.
print(type(list_1)) # Imprime el tipo de dato de list_1.
print(list_1[2]) # Imprime el tercer elemento de list_1.
list_1.append('HERMANA')
print(list_1) # Imprime list_1 después de agregar un nuevo elemento.

list=['SOLO',25,'HOLA',86,'SOLA','CASADO',6]

list_unida = list_1 + list
print(list_unida)  # Imprime la lista resultante de la unión de list_1 y list.

list_unida[1]='PERRO'
print(list_unida)  # Imprime list_unida después de modificar el segundo elemento.
print()
list_unida.remove('SOLA')
print(list_unida)  # Imprime list_unida después de eliminar el elemento 'SOLA'.

list_unida.max()  # Encuentra el valor máximo en list_unida.
print(list_unida)  # Imprime list_unida después de encontrar el máximo.
print()
''''3. Operaciones avanzadas
Comprensiones de listas: Crea nuevas listas de forma compacta:
Copy code
cuadrados = [x**2 for x in range(10)]

Filtrar elementos:
Copy code
pares = [x for x in mi_lista if x % 2 == 0]

Mapeo y transformación:
Copy code
dobles = list(map(lambda x: x*2, mi_lista))
'''