def calcular_importe_horas_estacionamiento(horas):
    tarifa_base = 6  # Costo de las primeras 4 horas
    tarifa_adicional = 2  # Costo por cada hora adicional

    if horas <= 4:
        importe_total = tarifa_base
    else:
        horas_adicionales = horas - 4
        importe_total = tarifa_base + (tarifa_adicional * horas_adicionales)

    return importe_total

# Solicitar el número de horas al usuario
horas_estacionamiento = int(input("Ingrese el número de horas de estacionamiento: "))

# Calcular el importe a pagar
importe_a_pagar = calcular_importe_horas_estacionamiento(horas_estacionamiento)

# Mostrar el importe a pagar
print("El importe a pagar es:", importe_a_pagar, "soles.")