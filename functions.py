import numpy as np
import matplotlib.pyplot as plt

def generar_serie(tamaño_muestra, distribucion, parametros):
    if distribucion == "uniforme":
        a, b = parametros
        return np.random.uniform(a, b, tamaño_muestra)
    
    elif distribucion == "exponencial":
        lambd = parametros[0]
        return np.random.exponential(1/lambd, tamaño_muestra)
    
    elif distribucion == "normal":
        media, desviacion = parametros
        return np.random.normal(media, desviacion, tamaño_muestra)

def crear_histograma(serie, num_intervalos):
    # Crear el histograma y obtener las frecuencias
    frecuencias, limites_intervalos = np.histogram(serie, bins=num_intervalos)

    # Mostrar tabla de frecuencias
    print("\nTabla de frecuencias:")
    print(f"{'Intervalo':<20}{'Frecuencia Observada':<20}")
    for i in range(len(frecuencias)):
        print(f"[{limites_intervalos[i]:.4f}, {limites_intervalos[i+1]:.4f})    {frecuencias[i]}")
    
    # Graficar histograma
    plt.hist(serie, bins=num_intervalos, edgecolor='black')
    plt.title(f"Histograma de {num_intervalos} intervalos")
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.show()