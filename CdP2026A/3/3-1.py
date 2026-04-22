# B: Representa los retardos (1 hora) o tiempo normal (0 horas) por cada viaje en orden.
B = [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0]
# C: Representa el costo o energía asociado a cada viaje del elevador E2.
C = [10,12,11,10,12]

def simular():
    # Inicialización de índices:
    # b: índice de la lista de retardos B
    # c: índice de la lista de costos C
    # viajes: total de viajes realizados
    # total: puntaje o ganancia acumulada
    b, c, viajes, total = 0, 0, 0, 0
    # listo: Diccionario que guarda la hora en la que cada elevador estará disponible para un nuevo viaje.
    listo = {'E2':1, 'E4':1, 'E1':1, 'E5':3}

    # El ciclo representa las horas de operación: de la hora 1 (01:00) a la 5 (05:00)
    for hora in range(1, 6):
        if viajes >= 15:
            break
        en_hora = 0 # Contador de viajes que inician en la hora actual
        
        # Orden de prioridad de los elevadores a evaluar por hora
        for elev in ['E2','E4','E1','E5']:
            if viajes >= 15 or en_hora >= 4:
                break
            
            # Si el elevador aún no está listo a la hora actual, se salta
            if listo[elev] > hora:
                continue
            # Condición especial: E5 solo opera a las 03:00 (hora == 3)
            if elev == 'E5' and hora != 3:   # E5 solo en 03:00
                continue
            # Condición especial: Se salta E1 a la 01:00 (hora == 1) para optimizar el uso de los retardos en B
            if elev == 'E1' and hora == 1:   # saltar E1 en 01:00 optimiza índices B
                continue

            # Obtener el retardo para el viaje actual y actualizar el índice b
            retardo = B[b % 15]; b += 1
            viajes += 1; en_hora += 1
            
            # Calcular la hora de llegada: hora de inicio + 1 hora de trayecto + posible retardo
            llegada = hora + 1 + retardo

            # Solo se puntúan los viajes que terminan dentro de la jornada laboral (hora <= 6)
            if llegada <= 6:
                if elev == 'E2':
                    # E2 suma 50 puntos menos el costo almacenado en C
                    total += 50 - C[c % 5]; c += 1
                elif elev == 'E4':
                    # E4 aporta una ganancia fija de 30 puntos por viaje
                    total += 30
                elif elev == 'E1':
                    # E1 aporta una ganancia fija de 20 puntos por viaje
                    total += 20
                elif elev == 'E5':
                    # E5 aporta una ganancia fija de 10 puntos por viaje
                    total += 10
                    
            # Actualizar la hora en la que el elevador volverá a estar disponible
            listo[elev] = llegada

    return total

# Ejecutar la simulación y guardar el total de puntos obtenidos
T = simular()
print(T)

# Evaluar el rendimiento basado en los puntos totales
if   T < 100:  print("Despido Inmediato")
elif T < 250:  print("Advertencia Severa (-20%)")
elif T < 450:  print("Rendimiento Aceptable")
elif T < 700:  print("Gestión Destacada (+15%)")
elif T < 900:  print("Héroe de la Logística (+50%)")
else:          print("Excelencia Suprema (+100% + Medalla)")
