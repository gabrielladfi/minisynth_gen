import math

def calcular_frecuencia_nota(octava, semitono):
    """
    Calcula la frecuencia de una nota musical en función de la octava y el número de semitonos
    desde el A4 (440 Hz).
    """
    # Frecuencia base (A4 = 440 Hz)
    A4 = 440.0
    # Distancia en semitonos desde A4
    distancia_semitonos = semitono + (octava - 4) * 12
    # Fórmula para la frecuencia de una nota
    frecuencia = A4 * (2 ** (distancia_semitonos / 12.0))
    return round(frecuencia, 2)

# Diccionario para las notas musicales desde C1 hasta B8
notas_musicales = {}
nombres_notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
nombres_notas_bemoles = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

# Rango de octavas de 1 a 8
for octava in range(1, 9):
    for i, nota in enumerate(nombres_notas):
        nombre_nota = f"{nota}{octava}"
        notas_musicales[nombre_nota] = calcular_frecuencia_nota(octava, i)

    # También añadimos los bemoles correspondientes
    for i, nota_bemol in enumerate(nombres_notas_bemoles):
        nombre_nota_bemol = f"{nota_bemol}{octava}"
        notas_musicales[nombre_nota_bemol] = calcular_frecuencia_nota(octava, i)

# Imprimir diccionario
for nota, frecuencia in notas_musicales.items():
    print(f' "{nota}": {frecuencia},')