valores = input().split()
tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])

def calculo(a,b): 
  padrao = 12
  dx = a * b 
  litros = dx / padrao
  return (f"{litros:.3f}")
  

resultado = calculo(tempo_gasto, velocidade_media)
print(resultado)
