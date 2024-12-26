# Sorteador de tareas v2
# 
# Modifico el programa a una forma más entendible que el que proporciona la IA
# Autor: Thevenin76
# 24/12/2024 Tenerife

import random

# Definimos los formularios y los asignados
formularios = ["Formulario 1", "Formulario 2", "Formulario 3"] # Arrays (empiezan por [] igual que PHP)
asignados = ["Víctor", "Rubén", "Markus"] # Arrays

# Barajamos los formularios de forma aleatoria
random.shuffle(formularios)

# Asignamos cada formulario a cada persona
#asignaciones = {asignados[i]: formularios[i] for i in range(len(asignados))} - Línea generada por la IA
print("Asignaciones de formularios:")

# Uso de bucles anidados
for i in range ((len(asignados))):
    asignaciones = { asignados[i]: formularios[i] } # Diccionario (va con llaves) , es igual a un array asociativo en PHP

    # Imprimimos los resultados
    for persona, formulario in asignaciones.items(): # Lo informamos en una tupla los elementos
        print(f"{persona} -> {formulario}")
