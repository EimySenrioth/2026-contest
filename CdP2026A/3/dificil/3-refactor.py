# B: eventos de basura espacial. 1 = retraso de 1h extra, 0 = viaje normal.
# Se consumen en orden: el primer elevador en despegar usa B[0], el segundo B[1], etc.
B = [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0]

# C: carga propia de E2 en cada viaje (toneladas que ya trae consigo, no cuentan).
# Se usa en orden circular: primer viaje de E2 usa C[0], segundo C[1], etc.
C = [10,12,11,10,12]

# Capacidad bruta de cada elevador en toneladas.
# E2 descuenta su carga propia (C) al momento del viaje.
CAP = {'E2':50, 'E4':30, 'E1':20, 'E5':10}

# Tabla de resultados laborales según toneladas entregadas.
# Cada tupla es (límite_superior_exclusivo, etiqueta).
RES = [
    (100,        "Despido Inmediato"),
    (250,        "Advertencia Severa"),
    (450,        "Rendimiento Aceptable"),
    (700,        "Gestión Destacada"),
    (900,        "Héroe de la Logística"),
    (float('inf'),"Excelencia Suprema"),
]

def simular():
    b     = 0   # índice actual en la lista B (basura espacial)
    c     = 0   # índice actual en la lista C (carga propia de E2)
    viajes = 0  # contador global de viajes despachados (máx 15)
    total  = 0  # toneladas netas entregadas a la estación

    # hora en que cada elevador queda libre para un nuevo viaje.
    # E5 no puede operar antes de las 03:00 (restricción de ventana).
    # E5 no puede operar antes de las 03:00 (restriccion de ventana).
    listo = {'E2':1, 'E4':1, 'E1':1, 'E5':3}

    # Ventana operativa: 01:00 a 05:00 (ultimo despegue posible).
    # Un viaje que sale a las 05:00 sin retraso llega justo a las 06:00 -> valido.
    for hora in range(1, 6):
        en = 0  # elevadores despachados en esta hora (max 4 simultaneos)
        print(f"\n{'='*55}")
        print(f"  HORA {hora:02d}:00  |  Viajes acumulados: {viajes}/15  |  Total: {total}t")
        print(f"{'='*55}")

        # Orden de prioridad: E2 > E4 > E1 > E5 (de mayor a menor carga neta).
        # Este orden tambien determina que indice de B consume cada elevador.
        for e in ['E2','E4','E1','E5']:

            # Respetar limite global de viajes y limite de despacho simultaneo.
            if viajes >= 15 or en >= 4:
                break

            # Saltar este elevador si:
            #   - aun no ha vuelto de un viaje anterior (listo[e] > hora)
            #   - es E5 fuera de su unica hora permitida
            #   - es E1 en la hora 01:00 (saltar E1 aqui alinea los indices B para
            #     que E2 y E4 consuman B=0 en las horas 04:00 y 05:00)
            if listo[e] > hora or (e=='E5' and hora!=3) or (e=='E1' and hora==1):
                if   listo[e] > hora:          motivo = f"ocupado hasta {listo[e]:02d}:00"
                elif e=='E5' and hora!=3:      motivo = "fuera de ventana (solo 03:00)"
                elif e=='E1' and hora==1:      motivo = "saltado para alinear indices B"
                print(f"  {e}  [SKIP]  -> {motivo}")
                continue

            # Consumir el siguiente evento de basura espacial (ciclo cada 15).
            ret = B[b % 15]
            b += 1; viajes += 1; en += 1

            # El viaje llega en hora+1 (normal) o hora+2 (con retraso).
            # Solo cuenta si llega a las 06:00 o antes.
            llegada = hora + 1 + ret
            if llegada <= 6:
                # E2 descuenta su carga propia del viaje actual.
                cargo = 50 - C[c % 5] if e == 'E2' else CAP[e]
                total += cargo
                c += (e == 'E2')  # avanzar indice C solo si despacho E2
                estado = f"+{cargo}t -> total={total}t"
            else:
                cargo = 0
                estado = f"llega {llegada:02d}:00 [TARDE, no cuenta]"

            retraso_str = f"B[{b-1}]=1 (+1h retraso)" if ret else f"B[{b-1}]=0 (sin retraso)"
            print(f"  {e}  [OK]  viaje#{viajes}  {retraso_str}  llegada={llegada:02d}:00  {estado}")

            # El elevador queda disponible cuando termina el viaje de subida.
            listo[e] = llegada

        print(f"  --- fin hora {hora:02d}:00: {en} despacho(s) esta hora ---")

    return total, viajes

T, viajes_usados = simular()

# Buscar el primer umbral que supere T para obtener el resultado laboral.
print(f"Viajes utilizados: {viajes_usados}/15")
print(T, next(r for m, r in RES if T < m))