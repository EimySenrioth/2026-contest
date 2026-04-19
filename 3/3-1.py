B = [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0]
C = [10,12,11,10,12]

def simular():
    b, c, viajes, total = 0, 0, 0, 0
    listo = {'E2':1, 'E4':1, 'E1':1, 'E5':3}

    for hora in range(1, 6):
        if viajes >= 15:
            break
        en_hora = 0
        for elev in ['E2','E4','E1','E5']:
            if viajes >= 15 or en_hora >= 4:
                break
            if listo[elev] > hora:
                continue
            if elev == 'E5' and hora != 3:   # E5 solo en 03:00
                continue
            if elev == 'E1' and hora == 1:   # saltar E1 en 01:00 optimiza índices B
                continue

            retardo = B[b % 15]; b += 1
            viajes += 1; en_hora += 1
            llegada = hora + 1 + retardo

            if llegada <= 6:
                if elev == 'E2':
                    total += 50 - C[c % 5]; c += 1
                elif elev == 'E4':
                    total += 30
                elif elev == 'E1':
                    total += 20
                elif elev == 'E5':
                    total += 10
            listo[elev] = llegada

    return total

T = simular()
print(T)
if   T < 100:  print("Despido Inmediato")
elif T < 250:  print("Advertencia Severa (-20%)")
elif T < 450:  print("Rendimiento Aceptable")
elif T < 700:  print("Gestión Destacada (+15%)")
elif T < 900:  print("Héroe de la Logística (+50%)")
else:          print("Excelencia Suprema (+100% + Medalla)")
