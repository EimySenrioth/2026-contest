from itertools import combinations

# Capacidad de cada elevador (toneladas por viaje)
elevadores = {1: 20, 2: 10, 3: 30, 4: 10}

# Horas restringidas: 4pm-8pm
# Asumiendo inicio a las 8am: hora 1=8am, ..., hora 9=4pm, hora 12=7pm
horas_restringidas = set(range(9, 13))

def hora_label(h):
    hora_real = 8 + h - 1
    if hora_real < 12:
        return f"{hora_real}:00 am"
    elif hora_real == 12:
        return "12:00 pm"
    else:
        return f"{hora_real - 12}:00 pm"

def mejor_combinacion(hora):
    max_elevadores = 2 if hora in horas_restringidas else 4
    mejor_combo = None
    mejor_toneladas = 0

    for cantidad in range(1, max_elevadores + 1):
        for combo in combinations(elevadores.keys(), cantidad):
            toneladas = sum(elevadores[e] for e in combo)
            if toneladas > mejor_toneladas:
                mejor_toneladas = toneladas
                mejor_combo = combo

    return mejor_combo, mejor_toneladas

def main():
    print("=" * 60)
    print("       OPTIMIZACIÓN DE ELEVADORES - 12 HORAS")
    print("=" * 60)
    print(f"\nCapacidad por elevador:")
    for elev, tons in elevadores.items():
        print(f"  Elevador {elev}: {tons} toneladas/viaje")

    print(f"\n{'Hora':<8} {'Tiempo':<12} {'Elevadores':<18} {'Restricción':<16} {'Toneladas'}")
    print("-" * 60)

    horario = []
    total = 0

    for h in range(1, 13):
        combo, toneladas = mejor_combinacion(h)
        restringida = h in horas_restringidas
        horario.append((h, combo, toneladas, restringida))
        total += toneladas

        restriccion_str = "[max 2 elevadores]" if restringida else ""
        print(f"Hora {h:<3} {hora_label(h):<12} {str(combo):<18} {restriccion_str:<16} {toneladas} t")

    print("-" * 60)
    print(f"\n{'TOTAL TRANSPORTADO:':>40} {total} toneladas")

    # Resumen
    horas_normales = [(h, t) for h, _, t, r in horario if not r]
    horas_rest = [(h, t) for h, _, t, r in horario if r]

    print(f"\nResumen:")
    print(f"  Horas sin restricción ({len(horas_normales)}h): "
          f"{horas_normales[0][1]} t/hora → {sum(t for _, t in horas_normales)} t")
    print(f"  Horas restringidas    ({len(horas_rest)}h): "
          f"{horas_rest[0][1]} t/hora → {sum(t for _, t in horas_rest)} t")
    print(f"  Total: {total} toneladas\n")

if __name__ == "__main__":
    main()