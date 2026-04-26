import re

def parsear_matriz(texto_matriz):
    filas = []
    for linea in texto_matriz.strip().split('\n'):
        linea = linea.strip()
        if not linea:
            continue
        # Extraer operaciones: números con + o -
        operaciones = re.findall(r'\d+[+\-]\d+', linea)
        fila = []
        for op in operaciones:
            if '+' in op:
                a, b = op.split('+')
                resultado = int(a) + int(b)
            else:
                a, b = op.split('-')
                resultado = int(a) - int(b)
            # Convertir a 1 si es 1, 0 si es 0 (o cualquier otro valor)
            fila.append(1 if resultado == 1 else 0)
        filas.append(fila)
    return filas

# ─── Entrada ────────────────────────────────────────────────────────────────
texto_A = """
1-0   2-2   0+1   3-3
0+0   1-0   2-2   0+1
4-4   0+1   1-0   2-2
0+1   3-3   0+0   1-0
"""

texto_B = """
1-0   0+0   0+1   2-2
0+1   1-0   3-3   0+1
5-5   0+1   1-0   4-4
0+1   2-2   0+0   1-0
1-1   0+0   2-2   0+1
"""

# ─── Parsear y evaluar ───────────────────────────────────────────────────────
A = parsear_matriz(texto_A)
B = parsear_matriz(texto_B)

print("═" * 40)
print("Matriz A resuelta (4×4):")
for fila in A:
    print(" ", fila)

print("\nMatriz B resuelta (5×4):")
for fila in B:
    print(" ", fila)

# ─── Comparar solo las primeras 4 filas de B ────────────────────────────────
print("\n" + "═" * 40)
print("Comparación posición a posición (AND lógico):")
print("─" * 40)

resultado = []
for i in range(4):
    fila_resultado = []
    for j in range(4):
        a_val = A[i][j]
        b_val = B[i][j]
        r = 1 if (a_val == 1 and b_val == 1) else 0
        fila_resultado.append(r)
        print(f"  [{i}][{j}]: A={a_val}  B={b_val}  → {' 1' if r == 1 else ' 0'}")
    resultado.append(fila_resultado)
    print()

# ─── Resultado final ─────────────────────────────────────────────────────────
print("═" * 40)
print("Matriz Resultado (4×4):")
for fila in resultado:
    print(" ", " ".join(map(str, fila)))