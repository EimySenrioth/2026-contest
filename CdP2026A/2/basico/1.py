import re

def parsear_matriz(texto_matriz):
    filas = []
    for linea in texto_matriz.strip().split('\n'):
        linea = linea.strip()
        if not linea:
            continue
        operaciones = re.findall(r'\d+[+\-]\d+', linea)
        fila = []
        for op in operaciones:
            if '+' in op:
                a, b = op.split('+')
                resultado = int(a) + int(b)
            else:
                a, b = op.split('-')
                resultado = int(a) - int(b)
            fila.append(1 if resultado == 1 else 0)
        filas.append(fila)
    return filas

# ─── Entrada ─────────────────────────────────────────────────────────────────
texto = """
1-1   0+1   2-2   0+0   3-3
0+1   1-0   3-3   0+0   2-2
2-2   0+1   1-0   4-4   0+0
0+0   2-2   0+1   1-0   5-5
1-1   0+0   2-2   0+1   1-0
"""

matriz = parsear_matriz(texto)

# ─── Print del proceso ────────────────────────────────────────────────────────
print("═" * 50)
print("Proceso de evaluación:")
print("─" * 50)

for i, linea in enumerate(texto.strip().split('\n')):
    linea = linea.strip()
    if not linea:
        continue
    operaciones = re.findall(r'\d+[+\-]\d+', linea)
    print(f"\nFila {i+1}:")
    for j, op in enumerate(operaciones):
        if '+' in op:
            a, b = op.split('+')
            res = int(a) + int(b)
        else:
            a, b = op.split('-')
            res = int(a) - int(b)
        binario = 1 if res == 1 else 0
        print(f"  [{i}][{j}]: {op} = {res} → {binario}")

# ─── Resultado final ──────────────────────────────────────────────────────────
print("\n" + "═" * 50)
print("Matriz Resultado (5×5):")
print("─" * 50)
for fila in matriz:
    print(" ".join(map(str, fila)))