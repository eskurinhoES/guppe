"""
Programa que lê uma velocidade em km/h e tranforma em Mts/s
"""
kmh = int(input('Digite a velocidade em kms/h: '))
mts = kmh / 3.6


print(f'A velocidade {kmh}km/h, equivale a {mts:.2f}mt/s')
