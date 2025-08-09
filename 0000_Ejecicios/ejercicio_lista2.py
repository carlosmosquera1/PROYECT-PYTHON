'''Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas
de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''

my_list = input('Ingrese nombre de la asignatura:')
my_list = my_list.split(',')
print(my_list)
for asignatura in my_list:
    nota = input(f'Ingrese nota de {asignatura}:')
    print(f'En {asignatura} has sacado {nota}')
   