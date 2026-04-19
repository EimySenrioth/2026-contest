def encriptar(texto: str) -> str:
    """
    Sirve para una frase con ESPACIO y dos palabras o una palabra
    No sopòrta numeros ni acentos
    Encripta un texto en dos fases:

    Fase 1 - Inversion de vocales por palabra:
        Para cada palabra, las vocales se extraen en orden, se invierten
        y se reinsertan en las mismas posiciones. Las consonantes no se tocan.
        Ejemplo: "Hola" -> vocales [o, a] invertidas [a, o] -> "Halo"

    Fase 2 - Intercambio de vocales abiertas (a, e, o):
        Recorre la cadena completa (incluyendo espacios) de izq. a der.
        Si encuentra una vocal abierta seguida de una letra (no espacio),
        las intercambia y salta 2 posiciones para no mover la vocal de nuevo.
        Si no hay letra a la derecha, no hace nada.
        Ejemplo: "Halo mondu" -> "Hlao mnodu"

    Args:
        texto: Texto a encriptar.

    Returns:
        Texto encriptado.
    """
    VOCALES: set[str]          = set("aeiouAEIOU")
    VOCALES_ABIERTAS: set[str] = set("aeoAEO")

    # --- FASE 1: Inversion de vocales por palabra ---
    palabras_fase1: list[str] = []

    for palabra in texto.split():               # split() maneja espacios multiples
        vocales_inv = [c for c in palabra if c in VOCALES][::-1]

        nueva, idx = list(palabra), 0
        for i in range(len(nueva)):
            if nueva[i] in VOCALES:
                nueva[i] = vocales_inv[idx]
                idx += 1

        palabras_fase1.append("".join(nueva))

    # --- FASE 2: Intercambio de vocales abiertas ---
    cadena = list(" ".join(palabras_fase1))
    i = 0
    while i < len(cadena) - 1:
        # Solo intercambia si el caracter de la derecha es una letra (no espacio)
        if cadena[i] in VOCALES_ABIERTAS and cadena[i + 1].isalpha():
            cadena[i], cadena[i + 1] = cadena[i + 1], cadena[i]
            i += 2      # saltar la vocal recien movida
        else:
            i += 1

    return "".join(cadena)


# --- TESTS ---
def run_tests() -> None:
    casos: list[tuple[str, str]] = [
        ("Hola mundo",  "Hlao mnodu"),
        ("Ojo de buey", "joO de buey"),
        ("hola",        "hlao"),
    ]

    print("-" * 42)
    print("Tests")
    print("-" * 42)
    for entrada, esperado in casos:
        salida = encriptar(entrada)
        ok = salida == esperado
        estado = "OK" if ok else f"FAIL (esperado: {esperado!r})"
        print(f"  {entrada!r:25} -> {salida!r}  {estado}")
        assert ok, f"Fallo en {entrada!r}: obtenido {salida!r}"
    print("-" * 42)
    print("Todos los tests pasaron OK")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    run_tests()
    print()
    texto = input("Ingresa el texto a encriptar: ")
    print(f"Texto encriptado: {encriptar(texto)}")