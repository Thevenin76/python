# Sorteador de tareas v1
# 
# Autor: hecho por IA MO4D - AZURE
# Prompt
# Genérame un script en python tal que sortee tres asignaciones de formularios :
# formulario 1 formulario 2 formulario 3
# A Victor, Rubén y Markus

import random

# Definimos los formularios y los asignados
formularios = ["Formulario 1", "Formulario 2", "Formulario 3"]
asignados = ["Víctor", "Rubén", "Markus"]

# Barajamos los formularios de forma aleatoria
random.shuffle(formularios)

# Asignamos cada formulario a cada persona
asignaciones = {asignados[i]: formularios[i] for i in range(len(asignados))}
print("Asignaciones de formularios:")

# Imprimimos los resultados
for persona, formulario in asignaciones.items():
    print(f"{persona} -> {formulario}")