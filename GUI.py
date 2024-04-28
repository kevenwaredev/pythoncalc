import tkinter as tk


# Funções da Calculadora
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def rest(a, b):
    return a % b


def restint(a, b):
    return a // b


# Função para lidar com o botão de cálculo
def calcular():
    a = float(valor1.get())
    operator = operacao.get()
    b = float(valor2.get())

    if operator == "+":
        resultado.set(add(a, b))
    elif operator == "-":
        resultado.set(sub(a, b))
    elif operator == "*":
        resultado.set(mult(a, b))
    elif operator == "/":
        resultado.set(div(a, b))
    elif operator == "%":
        resultado.set(rest(a, b))
    elif operator == "//":
        resultado.set(restint(a, b))
    else:
        resultado.set("Operação Inválida")


# Configuracão da janela
janela = tk.Tk()
janela.title("Calculadora")

# Frames
frame1 = tk.Frame(janela)
frame1.pack()

frame2 = tk.Frame(janela)
frame2.pack()

# Campos de entrada e rótulos
tk.Label(frame1, text="Primeiro Valor: ").grid(row=0, column=0)
valor1 = tk.Entry(frame1)
valor1.grid(row=0, column=1)

tk.Label(frame1, text="Operação +|-|*|/|//|%:").grid(row=0, column=2)
operacao = tk.Entry(frame1)
operacao.grid(row=0, column=3)

tk.Label(frame1, text="Segundo Valor:").grid(row=0, column=4)
valor2 = tk.Entry(frame1)
valor2.grid(row=0, column=5)

# Botao de cálculo
calcular_btn = tk.Button(frame2, text="Calcular", command=calcular)
calcular_btn.pack()

# Resultado
resultado = tk.StringVar()
resultado_label = tk.Label(frame2, textvariable=resultado)
resultado_label.pack()

# Executar loop
janela.mainloop()