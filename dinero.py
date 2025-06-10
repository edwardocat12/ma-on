def exchange_money(budget, exchange_rate):
    """
    Calcula el valor equivalente de una cantidad de dinero en una moneda extranjera.

    Parámetros:
    budget (float): La cantidad de dinero en la moneda original. Debe ser positivo.
    exchange_rate (float): La tasa de cambio del país. Esta tasa indica
                           cuántas unidades de la moneda original equivalen a 1 unidad
                           de la moneda local (extranjera).
                           Ejemplo: si 1 JPY = 0.0069 USD, entonces exchange_rate = 0.0069.
                           Debe ser un valor numérico positivo y mayor que cero.

    Retorna:
    float: El valor equivalente del presupuesto en la moneda extranjera.

    Lanza:
        ValueError: Si el presupuesto o la tasa de cambio no son números positivos.
    """
    if not isinstance(budget, (int, float)) or budget < 0:
        raise ValueError("El presupuesto debe ser un número positivo.")
    
    if not isinstance(exchange_rate, (int, float)) or exchange_rate <= 0:
        raise ValueError("La tasa de cambio debe ser un número positivo y mayor que cero.")
    
    foreign_currency_amount = budget / exchange_rate
    
    return foreign_currency_amount

# --- Datos de Tasas de Cambio (Valores aproximados al 8 de junio de 2025) ---
# Formato: {"MONEDA_LOCAL": TASA_VS_USD}
# Significa: 1 MONEDA_LOCAL = TASA_VS_USD USD
REAL_EXCHANGE_RATES_VS_USD = {
    "JPY": 0.0069,  # 1 JPY = 0.0069 USD (aprox. 1 USD = 144.9 JPY)
    "MXN": 0.052,   # 1 MXN = 0.052 USD (aprox. 1 USD = 19.23 MXN)
    "EUR": 1.14,    # 1 EUR = 1.14 USD (aprox. 1 USD = 0.877 EUR)
    "DOP": 0.017,   # 1 DOP = 0.017 USD (aprox. 1 USD = 58.82 DOP)
    "COP": 0.00024, # 1 COP = 0.00024 USD (aprox. 1 USD = 4166.67 COP)
    "BRL": 0.18,    # 1 BRL = 0.18 USD (aprox. 1 USD = 5.55 BRL)
    "GBP": 1.35,    # 1 GBP = 1.35 USD (aprox. 1 USD = 0.74 GBP)
    "CAD": 0.73,    # 1 CAD = 0.73 USD (aprox. 1 USD = 1.37 CAD)
}

# --- Interacción con el Usuario ---
if __name__ == "__main__":
    print("--- Calculadora de Divisas para Viajeros Frecuentes (con Tasas Actualizadas) ---")
    print("¡Hola Camila y Diego! Aquí pueden calcular el equivalente de su dinero.")
    print("Monedas soportadas (tasas vs. USD - aproximadas al 8 de junio de 2025):")
    
    # Mostrar las monedas disponibles y sus tasas relativas al USD
    print("----------------------------------------------------------------------")
    print(" Moneda Local | 1 Moneda Local = X USD (aprox.) | 1 USD = Y Moneda Local (aprox.)")
    print("----------------------------------------------------------------------")
    for currency, rate_vs_usd in REAL_EXCHANGE_RATES_VS_USD.items():
        if rate_vs_usd > 0:
            usd_to_currency_rate = 1 / rate_vs_usd
            print(f" {currency:<12} | {rate_vs_usd:<28.4f} | {usd_to_currency_rate:.2f}")
    print("----------------------------------------------------------------------")
    print("\n")

    while True:
        try:
            print("--- Nueva Conversión ---")
            # Supondremos que la moneda original de Camila y Diego es USD para simplificar
            # la selección de tasas predefinidas.
            nombre_moneda_original = "USD" 
            print(f"Su moneda original es: {nombre_moneda_original}")

            presupuesto_str = input(f"Ingrese su presupuesto en {nombre_moneda_original}: ")
            presupuesto = float(presupuesto_str)
            
            # Pedir al usuario que elija la moneda extranjera
            print("\nElija la moneda a la que desea cambiar de la lista anterior:")
            nombre_moneda_extranjera = input("Ingrese el código de la moneda extranjera (ej. JPY, EUR): ").upper()

            # Obtener la tasa de cambio de nuestra base de datos
            if nombre_moneda_extranjera in REAL_EXCHANGE_RATES_VS_USD:
                tasa_cambio = REAL_EXCHANGE_RATES_VS_USD[nombre_moneda_extranjera]
            elif nombre_moneda_extranjera == nombre_moneda_original: # Si la moneda extranjera es la misma
                tasa_cambio = 1.0 # La tasa es 1, se devuelve el mismo presupuesto
            else:
                raise ValueError(f"La moneda '{nombre_moneda_extranjera}' no está soportada en este momento.")

            # Realizar la conversión usando la función
            cantidad_convertida = exchange_money(presupuesto, tasa_cambio)

            print("\n--- Resultado de la Conversión ---")
            print(f"Usted tiene {presupuesto:.2f} {nombre_moneda_original}.")
            print(f"Con la tasa de cambio (1 {nombre_moneda_extranjera} = {tasa_cambio:.4f} {nombre_moneda_original}):")
            print(f"Obtendrá: {cantidad_convertida:.2f} {nombre_moneda_extranjera}.")
            
            # Preguntar si quieren hacer otra conversión
            otra_conversion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
            if otra_conversion != 's':
                break

        except ValueError as e:
            print(f"\n¡Error! Entrada inválida: {e}")
            print("Por favor, asegúrese de ingresar números válidos para el presupuesto y una moneda soportada.")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")
    
    print("\n--- ¡Gracias por usar la calculadora de divisas! ¡Felices viajes, Camila y Diego! ---")