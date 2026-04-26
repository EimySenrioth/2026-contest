vocales = "aeiouAEIOU"

frase = input("Ingresa una frase: ")
print(f"\nFrase original: '{frase}'")

# ─── PASO 1: Invertir vocales en cada palabra ───────────────────────────────
palabras = frase.split(' ')
palabras_inv = []

for palabra in palabras:
    posiciones = [i for i, c in enumerate(palabra) if c in vocales]
    letras_vocales = [palabra[i] for i in posiciones]
    letras_vocales_inv = letras_vocales[::-1]

    resultado = list(palabra)
    for pos, vocal in zip(posiciones, letras_vocales_inv):
        resultado[pos] = vocal

    palabra_inv = ''.join(resultado)
    palabras_inv.append(palabra_inv)

    print(f"\n  Palabra: '{palabra}'")
    print(f"    Vocales encontradas: {letras_vocales} en posiciones {posiciones}")
    print(f"    Vocales invertidas:  {letras_vocales_inv}")
    print(f"    Resultado paso 1:    '{palabra_inv}'")

cadena = ' '.join(palabras_inv)
print(f"\nDespués del Paso 1 (unida): '{cadena}'")

# ─── PASO 2: Cada vocal intercambia con el carácter a su derecha ─────────────
print(f"\n─── Paso 2: Swap vocal ↔ carácter derecho ───")
resultado = list(cadena)
i = 0
while i < len(resultado):
    if resultado[i] in vocales and i + 1 < len(resultado):
        antes = ''.join(resultado)
        resultado[i], resultado[i+1] = resultado[i+1], resultado[i]
        despues = ''.join(resultado)
        print(f"  pos {i}: '{antes[i]}' ↔ '{antes[i+1]}'  →  '{antes}' → '{despues}'")
        i += 2
    else:
        i += 1

final = ''.join(resultado)
print(f"\nResultado final: '{final}'")
#Hola mundo