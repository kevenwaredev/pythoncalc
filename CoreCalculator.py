#Funções da Calculadora


def add(a, b):
    return a + b

#Função de Subtrair

def sub(a, b):
    return a - b


#Função de Multiplicar


def mult(a, b):
    return a * b



#Função de Dividir


def div(a, b):
    return a / b




#Função de Resto da Divisão

def rest(a, b):
    return a % b




#Função de Resto da Divisão INTEIRA

def restint(a, b):
    return a // b




#Operações ocorrem aqui abaixo




a = None
b = None
operator = None

while(True):
    # get input values
    a = float(input("Digite o primeiro valor: "))
    operator = input("Digite a operação a ser feita: ")
    b = float(input("Digite o segundo valor:"))
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Argumento Invalido!")
        operator = None

    # decide function
    if (operator != None):
        if (operator == "+"):
            print("Soma: " ,a, "+ ",b, add(a, b))
        elif (operator == "-"):
            print("Subtração: " , a, "- ",b, sub(a, b))
        elif (operator == "*"):
            print("Multiplicação : " , a, " * ",b, mult(a, b))
        elif (operator == "/"):
            print("Divisão: " , a, "/ ",b, div(a, b))
        elif (operator == "%"):
            print("Resto da Divisão: " , a, "% ",b ,rest(a, b))
        elif(operator == "//"):
            print("Resto da Divisão Inteira" , a, "//", b , restint(a, b))
        else:
            print("Operação Invalida!")

    q = str(input("Sair? [S/n] "))
    if (q == "s" or q == "S"):
        break


