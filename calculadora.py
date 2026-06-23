# calculadora.py

def calcular(a, b, operacao):
    if operacao == "somar":
        return a + b
    if operacao == "subtrair":
        return a - b
    if operacao == "multiplicar":
        return a * b
    if operacao == "dividir":
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b
    raise ValueError(f"Operação desconhecida: {operacao}")
