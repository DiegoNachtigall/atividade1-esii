import math

# retorna o valor da soma entre os dois parâmetros
def sum(v1, v2) :
    return v1 + v2

# retorna o valor da subtração entre os dois parâmetros
def sub(v1, v2) :
    return v1 - v2

# retorna o valor da divisão entre os dois parâmetros
def div(v1, v2) :
    return v1 / v2

# retorna o valor da multiplicação entre os dois parâmetros
def mult(v1, v2) :
    return v1 * v2

# retorna o valor da raiz quadrada do valor recebido por parâmetro
def square(v1) :
    return math.sqrt(v1)

match(int(input("Selecione a operação desejada:\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Raiz Quadrada\n"))):
    case 1:
        print("A soma é:",sum(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: "))))
    case 2:
        print("A subtração é:",sub(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: "))))
    case 3:
        print("A divisão é:",div(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: "))))
    case 4:
        print("A multiplicação é:",mult(int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: "))))
    case 5:
        print("A raiz quadrada é:",square(int(input("Digite o valor: "))))
    case _:
        print("Operação inválida")

    

