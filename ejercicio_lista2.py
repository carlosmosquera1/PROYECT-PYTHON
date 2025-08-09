'''list_asignature = ['matematicas','fisica','quimica','Historia','lengua']
nota = []


for asigne in list_asignature:
	asignes = input("cual es su nota en "+asigne+ " ?")
nota.append(asignes)
for i in range(len(list_asignature)):
	print("en"+list_asignature[i] +"has sacado"+ nota[i])

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])
    '''
    
asignaturas = ['matematicas', 'fisica', 'quimica', 'Historia', 'lengua']
notas = []

for asignatura in asignaturas:
    nota = input(f"¿Cuál es tu nota en {asignatura}? ")
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
