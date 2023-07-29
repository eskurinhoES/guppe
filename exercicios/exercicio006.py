"""
Programa que lê uma temperatura em graus Celsius e converte para
graus faherenheit.
"""
celsius = float(input('Digite a temperatura em graus celsius: '))
faherenheit = celsius * (9.0 / 5.0) + 32.0
print(f'A temperatura {celsius}°C convertida para graus feherenheit é {faherenheit:.2f}°F')
