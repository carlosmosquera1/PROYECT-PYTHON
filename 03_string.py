### STRINGS ##

mu_string = 'Soy un string'
my_other_string = "Soy otro string"
print(len(mu_string))  # Imprime la longitud del string
print(len(my_other_string))  # Imprime la longitud del otro string
print(mu_string)  # Imprime el primer string
print(my_other_string)
print()

my_new_string_salto = " mi string \n es genial"
print(my_new_string_salto)  # Imprime el nuevo string con un salto de línea
print()
my_string_strip = '  mi string con espacios al inicio y al final   '
print(my_string_strip.strip())  # Elimina espacios en blanco al inicio y al final del string
print()
my_strig_lowers= 'soy string en letras minu'
print(my_strig_lowers.lower())  # Convierte el string a minúsculas
print()
string_tabulado = '\t soy un string con tabulacion'
print(string_tabulado)  # Imprime el string con tabulación
print()

string_mayu = ' soy un string en mayusculas'
print(string_mayu.upper())  # Convierte el string a mayúsculas
'''print(my_new_string.upper())  # Convierte el string a mayúsculas
print(my_new_string.replace("genial", "increíble"))  # Reemplaza "genial" por "increíble"
print(my_new_string.split())  # Divide el string en una lista de palabras
print(my_new_string.split(" "))  # Divide el string por espacios
print(my_new_string.split("e"))  # Divide el string por la letra "e"
print()'''

### FORMATEO DE STRINGS ###

name, surname, age = ' CARLOS', ' MOSQUERA', 25
print('Mi nombre es %s %s y mi edad es %d' % (name,surname,age))  # Formato antiguo de strings
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))  # Formato con .format()
print(f'Mi nombre es {name} {surname} y mi edad es {age}')  # Formato con f-strings (Python 3.6+)
print()


### DESEMPAQUETADO DE CARACTERES ###

caracteres = 'python'
a, b, c, d, e, f = caracteres  # Desempaqueta
print(a)  # Imprime el primer carácter
print(d)  # Imprime el segundo carácter
print()

## DIVISION DE STRINGS ##

lengueje_slice = caracteres[1:5]
print(lengueje_slice)  # Imprime una parte del string (desde el índice 1 hasta el 4)

lengueje_slice= caracteres[0:6:2]
print(lengueje_slice)  # Imprime una parte del string con un paso de 5 (no se muestra nada porque el paso es mayor que la longitud)

    ## REVERSE
    
lengueje_slice_reverse = caracteres[::-1]
print(lengueje_slice_reverse)  # Imprime el string al revés..

### FUNCIONES DEL SISTEMA ##

print(caracteres.capitalize()) # muestra la primera letra en mayuscula
print(caracteres.count('o'))  # Cuenta cuántas veces aparece 'o'
print(caracteres.endswith('n'))  # Verifica si el string termina con 'n
print(caracteres.startswith('p'))  # Verifica si el string comienza con 'p
print(caracteres.find('t'))  # Encuentra la posición de 't' en el string
print(caracteres.index('t'))  # Encuentra la posición de 't en el string (similar a find, pero lanza un error si no se encuentra)
print(caracteres.isalnum())  # Verifica si el string es alfanumérico (letras y números)
print(caracteres.isalpha())  # Verifica si el string contiene solo letras
print(caracteres.isdigit())  # Verifica si el string contiene solo dígitos
print(caracteres.islower())  # Verifica si el string está en minúsculas
print(caracteres.isupper())  # Verifica si el string está en mayúsculas
print(caracteres.replace('p', 'P'))  # Reemplaza 'p' por 'P'
print(caracteres.split('t'))  # Divide el string en una lista usando 't' como separador
print(caracteres.title())  # Convierte el       string a título (primera letra de cada palabra en mayúscula)
print()
