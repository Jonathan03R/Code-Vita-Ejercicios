

def calcular_distancia_total(cadena_buena, nombre):
    cadena_buena = list(cadena_buena)
    distancia_total = 0 
    ultima_letra_buena = cadena_buena[0]
    
    for letra in nombre:
        if letra in cadena_buena:
            ultima_letra_buena = letra
        else:
            
            distancia_minima = float('inf')
            mejor_letra = ultima_letra_buena
            
            for letra_buena in cadena_buena:
                distancia_actual = abs(ord(letra) - ord(letra_buena))
                
                
                if distancia_actual < distancia_minima:
                    distancia_minima = distancia_actual
                    mejor_letra = letra_buena
                elif distancia_actual == distancia_minima:
                
                    if abs(ord(ultima_letra_buena) - ord(letra_buena)) < abs (ord(ultima_letra_buena) - ord(mejor_letra) ):
                        mejor_letra = letra_buena
            distancia_total += distancia_minima
            ultima_letra_buena = mejor_letra
            
    return distancia_total

cadena_buena = "@HR*i{kcQl"
nombre = "Vyom"
print(calcular_distancia_total(cadena_buena, nombre))  # Salida: 10