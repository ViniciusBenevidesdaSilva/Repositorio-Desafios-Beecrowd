
# beecrowd | 1002: Área do Círculo

# A fórmula para calcular a área de uma circunferência é: area = π . raio ^2.
# Considerando para este problema que π = 3.14159:
# - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
# Saída
# Apresentar a mensagem "A=" seguido pelo valor da variável area,
# conforme exemplo abaixo, com 4 casas após o ponto decimal.
# Utilize variáveis de dupla precisão (double).

# Exemplos de Entrada	Exemplos de Saída
# 2.00                  A=12.5664
# 100.64                A=31819.3103
# 150.00                A=70685.7750


raio = float(input())

A = 3.14159 * raio ** 2

print(f'A={A:.4f}')


# PROBLEMA: 1002 - Área do Círculo
# RESPOSTA: Accepted
# LINGUAGEM: Python 3.9
# TEMPO: 0.034s
# TAMANHO: 71 Bytes
# MEMÓRIA: -
# SUBMISSÃO: 16/09/2022 16:14:59
