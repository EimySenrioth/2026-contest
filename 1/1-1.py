def encriptar_final(texto):
    vacales_abiertas = "aeoAEO"
    vocales_todas = "aeiouAEIOU"
    # SIRVE PARA PROBAR UNA FRASE con mas espacios y palabras, muchos espacios
    # --- FASE 1: Inversión de vocales por palabra ---
    palabras = texto.split(' ')
    fase1_palabras = []
    
    for p in palabras:
        # Extraer vocales de la palabra y revertirlas
        v_inv = [c for c in p if c in vocales_todas][::-1]
        p_lista = list(p)
        v_idx = 0
        for i in range(len(p_lista)):
            if p_lista[i] in vocales_todas:
                p_lista[i] = v_inv[v_idx]
                v_idx += 1
        fase1_palabras.append("".join(p_lista))

    # Unimos para tener la cadena de la Fase 1: "Halo mondu"
    cadena = list(" ".join(fase1_palabras))

    # --- FASE 2: Intercambio condicional (Solo si hay letra a la derecha) ---
    i = 0
    while i < len(cadena) - 1:
        char_actual = cadena[i]
        char_derecha = cadena[i+1]
        
        # REGLA: Vocal abierta + Carácter a la derecha que SEA LETRA (no espacio)
        if char_actual in vacales_abiertas and char_derecha.isalpha():
            # Intercambio
            cadena[i], cadena[i+1] = cadena[i+1], cadena[i]
            # Saltamos 2 posiciones para no procesar la misma vocal movida
            i += 2
        else:
            # Si es espacio, vocal cerrada o no hay letra: avanzar normal
            i += 1
            
    return "".join(cadena)

# --- PRUEBA ---
entrada = "Pato con chetos sin colesterol     triple cuatro four loco"
resultado = encriptar_final(entrada)

print(f"Entrada: {entrada}")
print(f"Salida:  {resultado}")