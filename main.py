from functions import * 
10
def main():
    # Pedir al usuario los parámetros
    tamaño_muestra = int(input("Ingrese el tamaño de la muestra (máx 1,000,000): "))
    if tamaño_muestra > 1000000:
        print("El tamaño de la muestra no debe exceder 1,000,000")
        return
    
    print("\nDistribuciones disponibles: 1) uniforme, 2) exponencial, 3) normal")
    distribucion = input("Seleccione la distribución (uniforme, exponencial, normal): ").lower()

    if distribucion == "uniforme":
        a = float(input("Ingrese el valor de a (mínimo): "))
        b = float(input("Ingrese el valor de b (máximo): "))
        parametros = (a, b)
    
    elif distribucion == "exponencial":
        lambd = float(input("Ingrese el valor de lambda (parámetro de tasa): "))
        parametros = (lambd,)
    
    elif distribucion == "normal":
        media = float(input("Ingrese la media: "))
        desviacion = float(input("Ingrese la desviación estándar: "))
        parametros = (media, desviacion)
    
    else:
        print("Distribución no válida.")
        return
    
    # Generar la serie
    serie = generar_serie(tamaño_muestra, distribucion, parametros)
    
    # Pedir el número de intervalos
    print("\nSeleccione el número de intervalos: 5, 10, 15, o 20")
    num_intervalos = int(input("Número de intervalos: "))
    if num_intervalos not in [5, 10, 15, 20]:
        print("Número de intervalos no válido.")
        return
    
    # Crear histograma
    crear_histograma(serie, num_intervalos)

if __name__ == "__main__":
    main()
