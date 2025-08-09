### CONDICIONALES ###

# Condicionales son estructuras de control que permiten ejecutar un bloque de código si se cumple una condición.

my_condition = False

if my_condition:
    print('Se ejecuta la condición if')
    
my_condition = 5 * 2

if my_condition == 10:
    print('Se ejecuta la condición if con valor numérico')
    
if my_condition > 10 and my_condition < 15 or (my_condition ==10 and my_condition != 10):
    print('es igual o mayor')

else:
    print('se ejecuta la del else')
    
my_striong= " que tal"

if my_striong:
    print(' No esta esta vacia')
    
elif not my_striong:
    print('esta vacia')

elif my_striong == 'hola que tal':
    print('no es igual a que tal')