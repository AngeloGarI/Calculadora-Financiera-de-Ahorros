def calcular_interés_compuesto(capital: float, tasa: float, tiempo: int) -> float:
    """
    Calcula el interés compuesto usando la formula del mismo.
    Fórmula: A = P * (1 + r/n)^(n*t)
    En este caso suponemos capitalización anual (n = 1).
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
            return meta * tasa / (( 1+ tasa ) ** tiempo - 1)

    except Exception as e:
        print("Error en cálculo de meta de ahorro:", e)
        return 0