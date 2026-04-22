import numpy as np

# ============================================================
# SOLUCIÓN: Detección de bloque 2x2 de unos en matrices
#
# Soluciòn:
#   1. Cada celda de la matriz contiene una operación aritmética
#      codificada como string.
#   2. Evaluar cada expresión: si el resultado es 1, la celda
#      vale 1; de lo contrario, vale 0.
#   3. Buscar el único bloque 2×2 compuesto íntegramente de 1s.
# ============================================================

# --- Paso 1: Definición de las matrices de operaciones ---
# Cada elemento es una expresión aritmética que resulta en 0 o 1.

matriz_a_ops = [
    ["5-5", "0+0", "8-8", "2-2", "0+0", "6-6", "1-1", "4-4", "0+0"], # F1
    ["3-3", "2-1", "0+1", "9-9", "7-7", "0+0", "8-8", "0+0", "2-2"], # F2
    ["1-1", "1+0", "3-2", "5-5", "0+0", "4-4", "0+0", "6-6", "0+0"], # F3
    ["0+0", "7-7", "9-9", "2-2", "0+0", "1-1", "5-5", "0+0", "8-8"], # F4
    ["4-4", "0+0", "6-6", "0+0", "3-3", "0+0", "7-7", "9-9", "0+0"], # F5
    ["2-2", "8-8", "0+0", "1-1", "5-5", "0+0", "4-4", "0+0", "6-6"], # F6
    ["0+0", "6-6", "4-4", "0+0", "8-8", "2-2", "0+0", "1-1", "5-5"], # F7
    ["9-9", "0+0", "7-7", "3-3", "0+0", "5-5", "0+0", "8-8", "0+0"], # F8
    ["0+0", "2-2", "0+0", "6-6", "4-4", "0+0", "9-9", "0+0", "3-3"]  # F9
]

matriz_b_ops = [
    ["4-4", "0+0", "9-9", "3-3", "1-1", "5-5", "0+0"],  # F1
    ["7-7", "5-4", "0+1", "8-8", "2-2", "0+0", "6-6"],  # F2
    ["1-1", "1+0", "10-9", "4-4", "0+0", "3-3", "9-9"], # F3
    ["0+0", "6-6", "2-2", "7-7", "5-5", "1-1", "0+0"],  # F4
    ["3-3", "8-8", "0+0", "1-1", "9-9", "4-4", "2-2"],  # F5
    ["5-5", "0+0", "3-3", "6-6", "0+0", "8-8", "1-1"],  # F6
    ["2-2", "4-4", "7-7", "0+0", "3-3", "0+0", "5-5"],  # F7
    ["0+0", "1-1", "5-5", "9-9", "4-4", "2-2", "0+0"]   # F8
]

matriz_c_ops = [
    ["6-6", "0+0", "3-3", "1-1"], # F1
    ["4-4", "9-8", "0+1", "5-5"], # F2
    ["2-2", "1+0", "7-6", "0+0"], # F3
    ["8-8", "2-2", "0+0", "9-9"]  # F4
]


# --- Paso 2: Convertir listas a arrays de NumPy ---
# Para el slicing 2D y las comparaciones vectorizadas.
matriz_a = np.array(matriz_a_ops)
matriz_b = np.array(matriz_b_ops)
matriz_c = np.array(matriz_c_ops)


# --- Paso 3: Función para evaluar las expresiones y construir la matriz binaria ---
def resolver_matriz(ops: list) -> np.ndarray:
    """
    Recorre cada celda de 'ops', evalúa la expresión aritmética
    y escribe 1 si el resultado es 1, o 0 en caso contrario.
    Retorna una matriz NumPy de enteros (0s y 1s).
    """
    filas = len(ops)
    cols  = len(ops[0])
    resultado = np.zeros((filas, cols), dtype=int)  # crea una matriz de la misma dimensión, pero llena de ceros.
    for i in range(filas): # Puntero para cada operación
        for j in range(cols):
            if eval(ops[i][j]) == 1:   #toma una cadena de texto y la interpreta como si fuera un comando de código real
                resultado[i, j] = 1   # si el resultado de la operacion es 1, la celda vale 1
    return resultado


# --- Paso 4: Función para localizar el bloque 2×2 de unos ---
def encontrar_bloque_2x2(matriz: np.ndarray) -> tuple:
    """
    Recorre la matriz con una ventana deslizante de 2×2.
    Retorna (fila, col) de la esquina superior-izquierda
    del primer bloque 2×2 compuesto de 1s.
    Lanza ValueError si no existe dicho bloque.
    """
    filas, cols = matriz.shape
    for i in range(filas - 1):         # Iterar filas dejando margen para el bloque
        for j in range(cols - 1):      # Iterar columnas dejando margen para el bloque
            if np.all(matriz[i:i+2, j:j+2] == 1):  # Verificar que las 4 celdas sean 1
                return (i, j)
    raise ValueError("No se encontro bloque 2x2 de unos.")


# --- Paso 5: Resolver cada nodo con el fin de evaluar las expresiones de cada matriz ---
nodo_a = resolver_matriz(matriz_a_ops)  # Resultado binario 9×9
nodo_b = resolver_matriz(matriz_b_ops)  # Resultado binario 8×7
nodo_c = resolver_matriz(matriz_c_ops)  # Resultado binario 4×4

# Mostrar los nodos resueltos y la posición del bloque 2×2 en cada uno
#El 2 x 2 comienza en la segunda fila y segunda columna de cada matriz
print("Nodo A resuelto (9x9):")
print(nodo_a)
print(f"  Bloque 2x2 en: {encontrar_bloque_2x2(nodo_a)}")

print("\nNodo B resuelto (8x7):")
print(nodo_b)
print(f"  Bloque 2x2 en: {encontrar_bloque_2x2(nodo_b)}")

print("\nNodo C resuelto (4x4):")
print(nodo_c)
print(f"  Bloque 2x2 en: {encontrar_bloque_2x2(nodo_c)}")

# --- Paso 6: Construir el nodo resultado ---
# El bloque común a los 3 nodos siempre es una matriz 2×2 de unos.
nodo_resultado = np.ones((2, 2), dtype=int)

print("\n" + "=" * 40)
print("NODO RESULTADO (bloque comun 2x2):")
print(nodo_resultado)
print("=" * 40)


# --- Paso 7: Tests automáticos para verificar la solución ---
# Primer test: Aquí  obligo a que el programa confirme que el bloque de 1s está exactamente en la posición (1, 1).
# Segundo test: Nodo Final sea una matriz 2 x 2 llena de 1s.

def run_tests() -> None:
    """Verifica que el bloque 2×2 de cada nodo esté en la posición esperada (1,1)."""
    assert encontrar_bloque_2x2(nodo_a) == (1, 1), "Bloque A incorrecto"
    assert encontrar_bloque_2x2(nodo_b) == (1, 1), "Bloque B incorrecto"
    assert encontrar_bloque_2x2(nodo_c) == (1, 1), "Bloque C incorrecto"
    assert np.array_equal(nodo_resultado, np.ones((2, 2), dtype=int))
    print("Todos los tests pasaron OK")

run_tests()