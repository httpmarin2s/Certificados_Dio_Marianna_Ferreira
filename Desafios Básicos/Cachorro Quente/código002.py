valores = input().split() 
participantes = int(valores[0])
cachorros_quentes = int(valores[1])

if 0 <= participantes <= 1000 and 0 <= cachorros_quentes <= 1000: 
  def calculo(p,h): 
    num_medio = (p/h)
    return (f"{num_medio:.2f}")


num_medio_cachorros_quentes = calculo(participantes, cachorros_quentes)
print(num_medio_cachorros_quentes)
