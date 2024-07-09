import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")

        # Frame para organização dos botões
        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.grid(row=1, column=0, columnspan=5)

        # Entrada e label de resultado
        self.entrada = tk.Entry(self.root, width=35, borderwidth=5, font=('Arial', 12))
        self.entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.label_resultado = tk.Label(self.root, text="", width=35, borderwidth=5, relief="sunken", anchor="e", font=('Arial', 12))
        self.label_resultado.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

        # Botões numéricos e operacionais
        botoes = [
            ('7', '8', '9', '+', 'C'),
            ('4', '5', '6', '-', '←'),
            ('1', '2', '3', '*', '/'),
            ('0', '.', '±', 'x^2', 'x^y'),
            ('sen', 'cos', 'tan', 'log', 'ln'),
            ('exp', '(', ')', 'π', 'e'),
            ('=', '', '', '', '')
        ]

        for linha, botoes_linha in enumerate(botoes):
            for coluna, simbolo in enumerate(botoes_linha):
                if simbolo == '':
                    continue
                tk.Button(self.frame_botoes, text=simbolo, padx=20, pady=10, width=5, command=lambda s=simbolo: self.processar_operacao(s)).grid(row=linha, column=coluna)

    def adicionar_caractere(self, caractere):
        entrada_atual = self.entrada.get()
        self.entrada.delete(0, tk.END)

        if caractere == '±':
            if entrada_atual.startswith('-'):
                self.entrada.insert(0, entrada_atual[1:])
            else:
                self.entrada.insert(0, '-' + entrada_atual)
        else:
            self.entrada.insert(0, entrada_atual + caractere)

    def processar_operacao(self, operacao):
        try:
            if operacao == 'C':
                self.entrada.delete(0, tk.END)
                self.label_resultado.config(text="")
            elif operacao == '←':
                self.entrada.delete(len(self.entrada.get()) - 1)
            elif operacao == '=':
                expressao = self.entrada.get().replace('π', str(math.pi)).replace('e', str(math.e))
                resultado = self.avaliar_expressao(expressao)
                self.label_resultado.config(text=resultado)
                self.entrada.delete(0, tk.END)  # Limpa a entrada após exibir o resultado
            else:
                self.adicionar_caractere(operacao)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def avaliar_expressao(self, expressao):
        try:
            return str(eval(expressao, {}, {}))
        except Exception as e:
            raise Exception("Expressão inválida")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
