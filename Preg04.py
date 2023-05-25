sueldo = float(input("Ingresar ganancia: "))

if sueldo <= 1000:
    porcentaje_donacion = 0.05
elif sueldo <= 1500:
    porcentaje_donacion = 0.07
elif sueldo <= 2000:
    porcentaje_donacion = 0.08
elif sueldo <= 5000:
    porcentaje_donacion = 0.10
else:
    porcentaje_donacion = 0.15

donacion = sueldo * porcentaje_donacion

print("la donación a realizar será:", donacion)