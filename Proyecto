def calcular_interés_compuesto(capital: float, tasa: float, tiempo: int) -> float: 
    """
    Calcula el interés compuesto usando la fórmula:
    A = P * (1 + r)^t
    Se supone que la capitalización es anual (n = 1).
    """
    try:
        if capital <= 0 or tasa < 0 or tiempo <= 0:
            raise ValueError("Los valores deben ser positivos.")
        return capital * (1 + tasa) ** tiempo
    except Exception as e:
        print("Error en cálculo de interés compuesto:", e)
        return 0


def calcular_meta_de_ahorro_(meta: float, tiempo: int, tasa: float = 0.0 ) -> float:
    """
    Calcula cuánto se debe ahorrar mensualmente para alcanzar una meta.
    Si la tasa > 0 se considera un interés compuesto aproximado.
    """
    try:
        if meta <= 0 or tiempo <= 0:
            raise ValueError("Los valores deben ser positivos.")

        if tasa == 0:
            return meta / tiempo
        else:
            return meta * tasa / ((1 + tasa) ** tiempo - 1)

    except Exception as e:
        print("Error en cálculo de meta de ahorro:", e)
        return 0


def plan_ahorro_mensual(ingreso: float, porcentaje: float) -> float:
    """
    Calcula cuánto ahorrar cada mes según un porcentaje del ingreso.
    """
    try:
        if ingreso <= 0 or porcentaje <= 0:
            raise ValueError("Los valores del ingreso y el porcentaje deben ser positivos.")
        return ingreso * (porcentaje / 100)
    except Exception as e:
        print("Error en el cálculo de plan de ahorro:", e)
        return 0

print("Calculadora Financiera")

while True:
    print("\nOpciones disponibles:")
    print("1. Usuario con ingreso fijo")
    print("2. Usuario con ingreso variable")
    print("3. Calcular interés compuesto")
    print("4. Calcular meta de ahorro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    #If para hacer el proceso de la ocíón que el usuario elija. 
    # Opción 1: Usuario con ingreso fijo
    if opcion == "1":
        ingreso = float(input("Ingrese su ingreso mensual fijo: "))
        porcentaje = float(input("¿Qué porcentaje desea ahorrar cada mes?: "))
        ahorro = plan_ahorro_mensual(ingreso, porcentaje)
        print(f"Usted ahorrará {ahorro:.2f} cada mes.")

    # Opción 2: Usuario con ingreso variable
    elif opcion == "2":
        meses = int(input("¿Cuántos meses desea registrar?: "))
        total_ahorro = 0
        for i in range(meses):
            ingreso = float(input(f"Ingreso del mes {i+1}: "))
            porcentaje = float(input("Porcentaje a ahorrar este mes: "))
            total_ahorro += plan_ahorro_mensual(ingreso, porcentaje)
        print(f"En {meses} meses habrá ahorrado un total de: {total_ahorro:.2f}")
    
    # Opción 3: Interés compuesto
    elif opcion == "3":
        capital = float(input("Ingrese el capital inicial: "))
        tasa = float(input("Ingrese la tasa de interés (ejemplo 0.05 para 5%): "))
        tiempo = int(input("Ingrese el tiempo en años: "))
        monto = calcular_interés_compuesto(capital, tasa, tiempo)
        print(f"El monto acumulado será: {monto:.2f}")

