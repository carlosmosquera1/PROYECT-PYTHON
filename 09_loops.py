### LOOPS ###

## WHILE LOOP ##

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2

if my_condition == 10:
    print('Este es el maximo del bucle')
else:
    print('No se ha alcanzado el maximo del bucle')
    
while my_condition < 20:
    print(my_condition)
    my_condition += 2
    print('detente')
   # break
if my_condition == 20:
   print('es igual a 16')
   print()
   
   
   ## FOR LOOP ##
   
   my_lista = [32,25,54,85,69,98]
   
   for i in my_lista:
       print(i)
       if i == 32:
           print("El numero esta en la lista")
       else:
           print(f"No se encontro el nummero:  {i}")
   
   

