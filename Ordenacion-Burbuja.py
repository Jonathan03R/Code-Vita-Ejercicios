
def ordenamient_burbuja(lista, ascendente):
    n = len(lista)
    numero_movimientas = 0
    lista_modificada = lista.copy()
    
    for i in range(n):
        for j in range(n -1 - i):
            if (ascendente and lista_modificada[j] > lista_modificada[j+1]) or (not ascendente and lista_modificada[j] < lista_modificada[j+1]):
                lista_modificada[j], lista_modificada[j+1] = lista_modificada[j+1], lista_modificada[j]
                numero_movimientas += 1
    return lista_modificada , numero_movimientas


lista = [1,25,4,5,6,7,65]

mov_asc = ordenamient_burbuja(lista, True)
mov_desc = ordenamient_burbuja(lista, False)

print(f'El {"ascendente" if mov_asc < mov_desc else "descendente" if mov_asc > mov_desc else "ambos"} es más rápido con {min(mov_asc, mov_desc)} movimientos.')
