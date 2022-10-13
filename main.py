#1.-Crea una variable llamada prof y asígnale el valor de 63.
prof = 63

#2.-Crea una variable llamada asig y asígnale el valor de 21.
asig = 21

#3.-Modifica el valor de prof por 64, e imprime la variable.
prof = 64
print(prof)

#4.-Escribe la palabra basket dentro de una variable llamada deporte.
deporte = "basket"

#5.-Escribe la palabra agua dentro de una variable llamada tipo.
tipo = "agua"

#6.-Crea una variable llamada hobby donde se almacenen las dos variables anteriores:deporte y tipo dando como resultado: "basket agua".
hobby = f"{deporte} {tipo}"

#7.-Escribe una lista llamada materia, compuesta por:lenguaje, inglés, matemáticas, historia y ciencias.
materia = ["lenguaje", "inglés", "matemáticas", "historia", "ciencias"]

#8.-Imprime el contenido de la lista
print(materia)

#9.-Imprime la materia ubicada en la tercera posición.
print(materia[2])

#10.-Añade a la lista el elemento artes, y ubícalo después de inglés.
materia.insert(2, "artes")

#11.-Muestra el contenido de la lista
materia

#12.-Usando remove, elimina de la lista materia los elementos historia y ciencias.
materia.remove("historia")
materia.remove("ciencias")

#13.-Usando pop, elimina de la lista materia el elemento ubicado en la posición 3.
materia.pop(3)

#14.-Crea una nueva lista llamada ramos, compuesta por música, religión, estadística y ciudadanía.
ramos = ["física", "religión", "estadística", "ciudadanía"]

#15.-Crea una nueva lista llamada asignaturas compuesta por los elementos de materia y ramos.
asignaturas = [materia + ramos]

#16.-Usando if verifica si la asignatura ciencias está en la lista asignaturas.
if "ciencias" in asignaturas:
    print("El ramo sí está en las asignaturas")
else:
    print("No está ese ramo en las asignaturas")

#17.-Crea una lista llamada primos_de_mersenne compuesta de los elementos:7, 3, 8191, 127, 31.
primos_de_mersenne = [7, 3, 8191, 127, 31]

#18.-Ordena la lista primos_de_mersenne de menor a mayor y de mayor a menor.
primos_de_mersenne.sort() #Menor > Mayor
primos_de_mersenne.sort(reverse = True) #Mayor > Menor
