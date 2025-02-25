import random
from statistics import *

print("Calculadora MMM")
escolha_nums = input("Você deseja digitar os números para calcular a moda, a media ou a mediana (caso contrário será calculada com uma lista aleatória) ? ")

while escolha_nums not in ["sim", "não"]:
  print("Opção inválida")
  escolha_nums = input("Você deseja digitar os números para calcular a moda, a media ou a mediana (caso contrário será calculada com uma lista aleatória) ? ")

if escolha_nums == "sim":
  nums = []
  prim_num = int(input("Digite um número de cada vez (mínimo de 5 e máximo de 20) : "))
  nums.append(prim_num)
  k = 0
  
  while k < 20:
    try:
        x = int(input("Digite outro número: "))
        nums.append(x)
        k += 1
        if k == 4:
          keep = input("Você atingiu o mínimo, deseja continuar? ")
          
          while keep not in ["sim", "não"]:
            print("Opção inválida") 
            keep = input("Você atingiu o mínimo, deseja continuar? ")
            
          if keep == "não":
            break
    except ValueError:
        print("Por favor, digite um número válido!")
        
  print(f"Sua lista de números é: {nums}")
else: 
  len_nums = random.randint(5, 20)
  nums = random.sample(range(1, 101), len_nums)
  
escolha = input("Você deseja calcular: moda, media ou mediana? ")

while escolha not in ["moda", "media", "mediana"]:
  print("Opção inválida")
  escolha = input("Você deseja calcular: moda, media ou mediana? ") 
  
def moda():
  print(nums)
  modas = multimode(nums)
  if len(modas) == len(nums):
    return print("Não há moda, todos os números aparecem com a mesma frequência.")
  elif len(modas) == 1:
    return print(f"A moda é: {modas[0]} (unimodal)")
  elif len(modas) == 2:
    return print(f"As modas são: {modas} (bimodal)")
  elif len(modas) == 3:
    return print(f"As modas são: {modas} (trimodal)")
  else:
    return print(f"As modas são: {modas} (plurimodal)")

def media():
  print(nums)
  return print(f"O resultado da media é: {sum(nums) / len(nums)}")

def mediana():
  print(sorted(nums))
  if len(nums) % 2 == 0:
    num_central = int(len(nums) // 2)
    nums_ordenados = sorted(nums)
    return print(f"O resultado da mediana é: {nums_ordenados[num_central-1]} e {nums_ordenados[num_central]}")
  else:
    num_central = int((len(nums) - 1) // 2)
    nums_ordenados = sorted(nums)
    return print(f"O resultado da mediana é: { nums_ordenados[num_central] }")
  
if escolha == "moda":
  moda()
elif escolha == "media":
  media()
elif escolha == "mediana":
  mediana()
else:
  print("Opção inválida")