### FUNCIONES ###

def my_funtion():
    print('esto es una funcion')
    
my_funtion() # llamamos la funcion my_funtion.


def sum_two_values(firts_name,second_name):
    print(firts_name + second_name / 10)
    
sum_two_values(12,135)

def sum_two_values_whit_retur(firs_name,second_name):
    my_sum = firs_name + second_name
    return my_sum

my_result = sum_two_values(1.2,2.0)
print(my_result)

my_resutl= sum_two_values_whit_retur(20,30)
print(my_resutl)


def print_name_wiht_default(name,surname,sobrenombre = 'sin sobrenombre'):
    print(f'Hola {name} {surname} {sobrenombre}')

print_name_wiht_default("CARLOS","MOSUQUERA")  # Llama a la función con los valores por defecto.
print_name_wiht_default('CARLOS','MOSQUERA','PUCHU')

def print_text(*text):
    print(text)
print_text('que tal','hola','como estas')
