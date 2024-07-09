def adicao (x, y):
    return x + y

def subtracao (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y

def div (x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por 0"
def main():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite sua escola (1/2/3/4): ")
        if escolha in ['1','2','3','4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == '1':
                print(f"{num1} + {num2} = {adicao(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtracao(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

            elif escolha == '4':
                resultado = divisao(num1, num2)
                if resultado == "Erro! Divisão por zero.":
                    print(resultado)
                else:
                    print(f"{num1} / {num2} = {resultado}")
        else:
            print("Entrada inválida. Por favor, escolha uma opção válida.")

        proxima_operacao = input("Deseja realizar outra operação? (s/n): ")
        if proxima_operacao.lower() != 's':
            break

if __name__ == "__main__":
    main()