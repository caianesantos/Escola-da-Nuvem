"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
def celsius_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_kelvin(c):
    return c + 273.15 

def fahrenheit_celsius(f):
    return (f - 32) *5/9

def fahrenheit_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_celsius(k):
    return k - 273.15

def kelvin_fahrenheit(k):
    return 1.8 * (k - 273) + 32

temperatura = float(input("Digite a temperatura atual: "))
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_conversao = input("Digite a unidade para qual deseja converter (C, F ou K): ").upper()

if unidade_origem == "C" and unidade_conversao == "F":
    print(f"A conversão de celsius para fahrenheit é: {celsius_fahrenheit(temperatura):.2f}°F")
elif unidade_origem == "C" and unidade_conversao == "K":
    print(f"A conversão de celsius para kelvin é: {celsius_kelvin(temperatura):.2f}°K")

elif unidade_origem == "F" and unidade_conversao == "C":
    print(f"A conversão de fahrenheit para celsius é: {fahrenheit_celsius(temperatura):.2f}°C")
elif unidade_origem == "F" and unidade_conversao == "K":
    print(f"A conversão de fahrenheit para kelvin é: {fahrenheit_kelvin(temperatura):.2f}°K")

elif unidade_origem == "K" and unidade_conversao == "C":
    print(f"A conversão de kelvin para celsius é: {kelvin_celsius(temperatura):.2f}°C")
elif unidade_origem == "K" and unidade_conversao == "F":
    print(f"A conversão de kelvin para fahrenheit é: {kelvin_fahrenheit(temperatura):.2f}°F")

elif unidade_origem == unidade_conversao:
    print(f"A temperatura continua a mesma: {temperatura:.2f}°{unidade_origem}")

else:
    print(f"Unidade de origem ({unidade_origem}) ou unidade de conversão ({unidade_conversao}) não existente. Digite uma unidade válida (C, F ou K).")