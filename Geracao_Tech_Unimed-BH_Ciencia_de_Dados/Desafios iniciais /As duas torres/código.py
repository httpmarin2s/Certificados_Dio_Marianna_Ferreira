entrada = input().split()
# esse código aqui vai repartir cada um dos itens 

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

if 0 < distancia < 10000 and 0 < diametro1 < 100 and 0 < diametro2 < 100: 
  def ICM(distancia, diametro1, diametro2): 
    calculo = distancia/(diametro1 + diametro2)
    return (f"{calculo:.2f}")

resultado_icm = ICM(distancia, diametro1, diametro2)
print(resultado_icm)
