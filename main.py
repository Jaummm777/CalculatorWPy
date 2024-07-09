import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.operacoes = {
            '+': self.adicao,
            '-': self.subtracao,
            '*': self.multiplicacao,
            '/': self.divisao
        }
        self.create_widgets()

    def adicao(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        if y != 0:
            return x / y
        else:
            self.mostrar_erro("Divisão por zero não é permitida")
            return None

    def create_widgets(self):
        self.entrada_num1 = tk.Entry(self.root, width=10)
        self.entrada_num1.grid(row=0, column=0, padx=5, pady=5)

        self.entrada_num2 = tk.Entry(self.root, width=10)
        self.entrada_num2.grid(row=0, column=2, padx=5, pady=5)

        self.label_resultado = tk.Label(self.root, text="Resultado:")
        self.label_resultado.grid(row=1, column=1, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        row, col = 2, 0
        for simbolo, operacao in self.operacoes.items():
            botao = tk.Button(self.root, text=simbolo, command=lambda op=operacao: self.calcular(op))
            botao.grid(row=row, column=col, padx=5, pady=5)
            col += 1

    def calcular(self, operacao):
        try:
            num1 = self.obter_numero(self.entrada_num1)
            num2 = self.obter_numero(self.entrada_num2)
            resultado = operacao(num1, num2)
            if resultado is not None:
                self.label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.mostrar_erro("Por favor, insira números válidos")

    def obter_numero(self, entrada):
        return float(entrada.get())

    def mostrar_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
