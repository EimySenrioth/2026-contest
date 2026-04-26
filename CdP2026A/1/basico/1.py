def invertir_vocales(palabra):
    vocales = "aeiouAEIOU"
    posiciones = [i for i, c in enumerate(palabra) if c in vocales]
    letras_vocales = [palabra[i] for i in posiciones]
    letras_vocales.reverse()
    
    resultado = list(palabra)
    for pos, vocal in zip(posiciones, letras_vocales):
        resultado[pos] = vocal
    
    return ''.join(resultado)

frase = input("Ingresa una frase: ")

# Dividir cada palabra en dos mitades
palabras_resultado = []
for palabra in frase.split(' '):
    mitad = len(palabra) // 2
    primera = invertir_vocales(palabra[:mitad])
    segunda = invertir_vocales(palabra[mitad:])
    palabras_resultado.append(primera + segunda)

print(''.join(palabras_resultado))
#Holamundo
