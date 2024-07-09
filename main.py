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
            messagebox.showerror("Erro", "Divisão por zero não é permitida")
            return None

    def create_widgets(self):
        self.entry1 = tk.Entry(self.root, width=10)
        self.entry1.grid(row=0, column=0, padx=5, pady=5)

        self.entry2 = tk.Entry(self.root, width=10)
        self.entry2.grid(row=0, column=2, padx=5, pady=5)

        self.result_label = tk.Label(self.root, text="Resultado:")
        self.result_label.grid(row=1, column=1, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        row, col = 2, 0
        for op in self.operacoes:
            button = tk.Button(self.root, text=op, command=lambda op=op: self.calculate(op))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1

    def calculate(self, op):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            resultado = self.operacoes[op](num1, num2)
            if resultado is not None:
                self.result_label.config(text=f"Resultado: {resultado}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
