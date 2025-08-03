### DICCCIONARIOS ###

my_dic = dict() # Crea un diccionario vacío.

my_uther_dicm ={} # Crea un diccionario vacío.

print(type(my_uther_dicm))  # Imprime el tipo de dato de my_uther_dicm, que es un diccionario.
print(type(my_dic))

my_uther_dicm = {'nombre':'CARLOS','apellido':'MOSQUERA','edad':25,'altura':1.75}  # Crea un diccionario con elementos.

my_dic = {
    'nombre':'CARLOS',
    'apellido':'MOSQUERA',
    'edad':25,
    'altura':1.75,
    'TAREAS':{
        'TAREA1':'EJERCICIO DE TUPLAS',
        'TAREA2':'EJERCICIO DE DICCIONARIOS',
        'TAREA3':'EJERCICIO DE CONJUNTOS',
        'TAREA4':'EJERCICIO DE LISTAS',
        'TAREA5':'EJERCICIO DE CADENAS'
    }
    }  # Crea un diccionario con elementos.
print(my_uther_dicm)
print(my_dic)  # Imprime el contenido de my_uther_dicm.

print(len(my_uther_dicm))  # Imprime la longitud del diccionario my_uther_dicm.
print(len(my_dic))  # Imprime la longitud del diccionario my_dic.s

print(my_dic['apellido'])  # Imprime el valor asociado a la clave 'apellido' en my_dic.
my_dic['nombre'] = 'SERGIO'  # Cambia el valor asociado a la clave 'nombre' en my_dic.
print(my_dic['nombre'])  # Imprime el nuevo valor asociado a la clave 'nombre'.
print(my_dic['TAREAS']['TAREA1'])  # Imprime el valor asociado a la clave 'TAREA1' dentro del diccionario anidado 'TAREAS'.
#print(my_dic[1])

my_dic['Calle'] = 'La calle los Mosqueras'  # Agrega una nueva clave 'Calle' con su valor al diccionario my_dic.
print(my_dic)  # Imprime el diccionario my_dic después de agregar la nueva clave.
print(my_dic['Calle'])  # Imprime el valor asociado a la nueva clave 'Calle'.

del my_dic['TAREAS']  # Elimina la clave 'TAREAS' del diccionario my_dic.
print(my_dic)  # Imprime el diccionario my_dic después de eliminar la clave
print(my_dic.keys())  # Imprime las claves del diccionario my_dic.
print(my_dic.values())  # Imprime los valores del diccionario my_dic.
print(my_dic.items())  # Imprime los pares clave-valor del diccionario my_dic.
print(my_dic.get('nombre'))  # Imprime el valor asociado a la clave 'nombre' en my_dic.
print(my_dic.get('apellido'))  # Imprime el valor asociado a la clave 'apellido' en my_dic.
print(my_dic.get('edad'))  # Imprime el valor asociado a la clave 'edad' en my_dic.
print(my_dic.get('altura'))  # Imprime el valor asociado a la clave 'altura' en my_dic.
print()


print('carlos'in my_dic)  # Verifica si 'carlos' está en las claves del diccionario my_dic (debería ser False).
if('carlos' not in my_dic):
    print('No existe la clave "carlos" en el diccionario.')
else: 
    print('La clave "carlos" existe en el diccionario.')
print('CARLOS   ' in my_dic)  # Verifica si 'carlos' está en las claves del diccionario my_dic (debería ser True).
print(my_dic)
my_dic['nombre']='carlos'   # Agrega una nueva clave 'nomvre' con su valor al diccionario my_dic.
my_dic['nombre']
print(my_dic)  # Imprime el diccionario my_dic después de agregar la nueva clave.

print(25 in my_dic)  # Verifica si 'edad' está en las claves del diccionario my_dic (debería ser True).
#print('edad' in my_dic)  # Verifica si 'edad' está en las claves del diccionario my_dic (debería ser True).
print()

my_new_dic = dict.fromkeys(['nombre', 'apellido', 'edad', 'altura'], 'Desconocido')  # Crea un nuevo diccionario con claves y un valor por defecto.
print(my_new_dic)  # Imprime el nuevo diccionario con claves y un valor por defecto.
my_new_dic['nombre'] = 'Sergio'  # Cambia el valor asociado a la clave 'nombre' en el nuevo diccionario.

print(my_new_dic)  # Imprime el nuevo diccionario después de cambiar el valor de 'nombre'.

my_new_dic['apellido'] = 'Mosquera'  # Cambia el valor asociado a la clave 'apellido' en el nuevo diccionario. 

print(my_new_dic)  # Imprime el nuevo diccionario después de cambiar el valor de 'apellido'.
'''
my_new_dic['edad'] = 25  # Cambia el valor asociado a la clave 'edad' en el nuevo diccionario.

print(my_new_dic)  # Imprime el nuevo diccionario después de cambiar el valor de 'edad'.

my_new_dic['altura'] = 1.75  # Cambia el valor asociado a la clave 'altura' en el nuevo diccionario.

print(my_new_dic)  # Imprime el nuevo diccionario después de cambiar el valor de 'altura'.)

print(my_new_dic['nombre'])  # Imprime el valor asociado a la clave 'nombre' en el nuevo diccionario.

print(my_new_dic['apellido'])  # Imprime el valor asociado a la clave 'apellido' en el nuevo diccionario.

print(my_new_dic['edad'])  # Imprime el valor   asociado a la clave 'edad' en el nuevo diccionario.

print(my_new_dic['altura'])  # Imprime el valor asociado a la clave 'altura
'''

my_new_dic = dict.fromkeys(my_dic)

my_list = ['nombre','apellido','edad','altura']  # Crea una lista con claves.
print(list(my_new_dic))
print(tuple(my_new_dic))  # Convierte el diccionario my_new_dic en una tupla.
print(set(my_new_dic))  # Convierte el diccionario my_new_dic en un conjunto.
#my_new_dic = dict.fromkeys(my_dic,)