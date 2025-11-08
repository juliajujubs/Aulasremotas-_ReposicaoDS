def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero"
    else:
        return "Operação inválida"

if __name__ == "__main__":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(numero1, numero2, operacao)
    print("Resultado:", resultado)
