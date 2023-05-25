tipo_de_bus=1
distancia=24
capacidad=15
if tipo_de_bus == 1 :
  if capacidad <= 20: 
        costo=2*distancia
        costo_total=costo*capacidad;
        print(f'Costo de pasaje por persona: {costo}')
        print(f'Costo total de viaje: {costo_total}')
        
  else:
    print("cantidad no permitida")

elif tipo_de_bus == 2:
  if capacidad <= 20: 
        costo=2.5*distancia
        costo_total=costo*capacidad
        print(f'Costo de pasaje por persona: {costo}')
        print(f'Costo total de viaje: {costo_total}')
  else:
    print("cantidad no permitida")

elif tipo_de_bus == 3:
  if capacidad <= 30:
        costo=3*distancia
        costo_total=costo*capacidad
        print(f'Costo de pasaje por persona: {costo}')
        print(f'Costo total de viaje: {costo_total}')
  else:
    print("cantidad no permitida")