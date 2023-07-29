"""
Programa que lê uma tempreratura em graus Fahrenheit e mostra ela
convertida pra graus Celsius.
"""
fahrenheit = float(input('Digite a temperatura em graus Farhenheit que deseja converter: '))
celsius = 5.0 * (fahrenheit - 32) / 9.0
print(f'A temperatura {fahrenheit:.2f}°F corresponde a {celsius:.2f}°C')
