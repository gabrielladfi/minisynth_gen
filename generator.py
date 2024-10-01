import numpy as np
import scipy.signal as signal
import wave
import struct
from dict_notas import notas 

def generar_senal_cuadrada(nota_hz, duracion_s=4, sample_rate=44100, amplitud=22767):
    # Tiempo total
    t = np.linspace(0, duracion_s, int(sample_rate * duracion_s), endpoint=False)

    #Calcular los valores de los armónicos
    amplitud_1 = amplitud/8
    amplitud_2 = amplitud/16
    # Generar la señal cuadrada con dos armónicos
    senal_1 = amplitud * signal.square(2 * np.pi * nota_hz * (t+2)) 
    senal_2 = amplitud_1 * signal.square(3 * np.pi * nota_hz * (t+2))
    senal_3 = amplitud_2 * signal.square(4 * np.pi * nota_hz * (t+2))
    senal_cuadrada = senal_1 + senal_2 + senal_3

    # Convertir a enteros de 16 bits para WAV
    senal_cuadrada = senal_cuadrada.astype(np.int16)

    # Crear el archivo WAV
    nombre_archivo = f'senal_cuadrada_{nota_hz}Hz.wav'
    with wave.open(nombre_archivo, 'w') as archivo_wav:
        #Manejo de canales
        archivo_wav.setnchannels(1)
        archivo_wav.setsampwidth(2)
        archivo_wav.setframerate(sample_rate)
        # Escribir los datos al archivo
        for muestra in senal_cuadrada:
            archivo_wav.writeframes(struct.pack('h', int(muestra)))

    return nombre_archivo
#Usamos 110 Hz para emular el sonido de C2 (Do2)
archivo_wav = generar_senal_cuadrada(110)
print(f'Archivo guardadp: {archivo_wav}')
