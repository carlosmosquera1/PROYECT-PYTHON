### LISTAS ##

my_list = list()  # Crea una lista vacía.

my_other_list = [25,'CARLOS','MOSQUERA','1.75']  # Crea una lista con elementos.

my_list= [20,30,60,40,50,90]  # Inicializa my_list como una lista vacía.
print(type(my_list))  # Imprime el tipo de dato de my_list.
print(type(my_other_list))  # Imprime el tipo de dato de my_other_list.,

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])  # Imprime los elementos de la lista por índice.
print(my_other_list[-1])  # Imprime el último elemento de la lista usando índice negativo.
print(my_other_list[-2])  # Imprime el penúltimo elemento de la lista usando índice negativo.
print(my_other_list[-3])  # Imprime el antepenúlt   mo elemento de la lista usando índice negativo.
print(my_other_list[-4])  # Imprime el primer elemento de la lista usando índice negativo.
##print(my_other_list[-5])  # Imprime un error porque no hay quinto elemento negativo.+
print()

age,nombre,surname,height = my_other_list  # Desempaqueta los elementos de la lista en variables.
print(age)  # Imprime la edad.
print(nombre)  # Imprime el nombre.
print(surname)  # Imprime el apellido.
print(height)  # Imprime la altura.
print()

print(my_list + my_other_list)

my_other_list.append('PUCHU')  # Agrega un nuevo elemento al final de my_other_list.
print(my_other_list)  # Imprime my_other_list después de agregar el nuevo elemento.
print()
my_other_list.insert(2, 'PUCHU')  # Inserta 'PUCHU' en la posición 2 de my_other_list.
print(my_other_list)  # Imprime my_other_list después de la inserción.
print()
my_other_list.remove('PUCHU')  # Elimina el primer elemento 'PUCHU' de my_other_list.
print(my_other_list)  # Imprime my_other_list después de eliminar 'PUCHU'.
print()
my_other_list.pop()  # Elimina el último elemento de my_other_list.
print(my_other_list)  # Imprime my_other_list después de eliminar el último elemento.
print()
my_other_list.pop(1)  # Elimina el elemento en la posición 1 de my_other_list.
print(my_other_list)  # Imprime my_other_list después de eliminar el elemento en la posición 1.
print()
'''my_other_list.sort()  # Ordena my_other_list en orden ascendente.
print(my_other_list)  # Imprime my_other_list después de ordenar.
print()'''
my_other_list.reverse()  # Invierte el orden de los elementos en my_other_list.
print(my_other_list)  # Imprime my_other_list después de invertir el orden.
print()

my_other_list[1]='MARIO'
print(my_other_list)  # Modifica el elemento en la posición 1 de my_other_list y lo imprime.

my_list = 'Hola mundo'
print(my_list)  # Imprime el contenido de my_list, que ahora es un string


