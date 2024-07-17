Aquecimento

1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.
!pip install matplotlib==3.7.1

2. Escreva um código para importar a biblioteca numpy com o alias np.
import numpy.pyplot as np

3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.



from random import sample

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

sample(lista, 1)

4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.

from random import randrange, sample

lista = []

for i in range(0, 100):
  lista.append(randrange(100))

sample(lista,1)

5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.


import math

x = int(input("Digite um número positivo para ser a base da potencia:"))
y = int(input("Digite um número positivo para ser a expoente da potencia:"))
print(f"\n A potendia de {x}elevado a {y} é igual a {math.pow(x, y)}")

Aplicando a projetos