from itertools import combinations, product

ELEVATORS   = {1: 20, 2: 10, 3: 30, 4: 10}
HOURS       = list(range(8, 20))
LOSS_PATTERN = [0.10, 0.01, 0.0, 0.60, None]

def net_cargo(gross: float, trip_num: int) -> float:
    idx = (trip_num - 1) % len(LOSS_PATTERN)
    spec = LOSS_PATTERN[idx]
    return gross - 0.002 if spec is None else gross * (1 - spec)

def max_elevators(hour: int) -> int:
    return 2 if 16 <= hour <= 19 else 4

def eval_schedule(schedule: list[list[int]]) -> float:
    """Evalúa un horario completo y devuelve la carga neta total."""
    counts = {eid: 0 for eid in ELEVATORS}
    total_net = 0.0
    for chosen in schedule:
        for eid in chosen:
            counts[eid] += 1
            gross = ELEVATORS[eid]
            total_net += net_cargo(gross, counts[eid])
    return total_net

def all_subsets(hour: int) -> list[list[int]]:
    """Genera todos los subconjuntos válidos de ascensores para una hora."""
    limit = max_elevators(hour)
    eids  = list(ELEVATORS.keys())
    result = [[]]  # opción: no usar ninguno
    for r in range(1, limit + 1):
        for combo in combinations(eids, r):
            result.append(list(combo))
    return result

def brute_force() -> tuple[float, list]:
    """
    Explora todas las combinaciones posibles hora a hora usando
    programación dinámica (DP) sobre el estado de viajes de cada ascensor.
    Estado: tupla (viajes_A1, viajes_A2, viajes_A3, viajes_A4)
    """
    # dp[estado] = max carga neta alcanzable desde ese estado
    # Usamos DP hacia adelante hora por hora
    
    init_state = (0, 0, 0, 0)
    # dp: estado → (carga_neta_acumulada, lista_de_decisiones)
    dp = {init_state: (0.0, [])}

    eids = list(ELEVATORS.keys())

    for i, hour in enumerate(HOURS):
        new_dp = {}
        subsets = all_subsets(hour)

        for state, (acc_net, decisions) in dp.items():
            for chosen in subsets:
                counts = list(state)
                gain   = 0.0
                valid  = True

                for eid in chosen:
                    idx_e         = eid - 1
                    counts[idx_e] += 1
                    gross          = ELEVATORS[eid]
                    gain          += net_cargo(gross, counts[idx_e])

                new_state = tuple(counts)
                new_total = acc_net + gain

                if new_state not in new_dp or new_dp[new_state][0] < new_total:
                    new_dp[new_state] = (new_total, decisions + [chosen])

        dp = new_dp
        print(f"  Hora {hour}:00 procesada — estados explorados: {len(dp)}")

    best_net  = max(v[0] for v in dp.values())
    best_sched = max(dp.values(), key=lambda v: v[0])[1]
    return best_net, best_sched

if __name__ == "__main__":
    print("Buscando solución óptima por programación dinámica...\n")
    best_net, best_schedule = brute_force()

    print(f"\n{'='*50}")
    print(f"  CARGA NETA MÁXIMA ABSOLUTA: {best_net:.6f} t")
    print(f"{'='*50}")

    counts = {eid: 0 for eid in ELEVATORS}
    total_bruto = 0.0
    for hour, chosen in zip(HOURS, best_schedule):
        hora_net = 0.0
        hora_bruto = 0.0
        for eid in chosen:
            counts[eid] += 1
            gross = ELEVATORS[eid]
            net   = net_cargo(gross, counts[eid])
            hora_net   += net
            hora_bruto += gross
            total_bruto += gross
        ascensores = [f"A{e}" for e in chosen] if chosen else ["ninguno"]
        print(f"  {hour}:00 → {', '.join(ascensores):20} | bruto: {hora_bruto:.1f}t | neto hora: {hora_net:.4f}t")

    print(f"\n  Bruto total : {total_bruto:.2f} t")
    print(f"  Pérdidas    : {total_bruto - best_net:.6f} t")
    print(f"  NETO TOTAL  : {best_net:.6f} t")
    print(f"  Viajes A1={counts[1]}, A2={counts[2]}, A3={counts[3]}, A4={counts[4]}")

