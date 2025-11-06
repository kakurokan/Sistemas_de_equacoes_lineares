from sympy import *


class IteracoesExcedidas(Exception):
    pass


def criar_matriz(elementos):
    matrix = [sympify(n) for n in elementos]
    return Matrix(matrix)


def norma(matriz_a, matriz_b):
    resultado = matriz_b - matriz_a
    return max(resultado, key=abs)


def gauss_seidel(n, coeficiente, coluna, tol, n_max):
    k = 0
    elementos_x = []
    for i in range(n):
        elementos_x.append(0)
    matriz_x = criar_matriz(elementos_x)
    matriz_a = coeficiente.copy()
    matriz_b = coluna.copy()

    while k < n_max:
        x_anterior = matriz_x.copy()
        for i in range(n):
            soma = 0
            for j in range(n):  # calcula cada linha, ou seja o valor de xi
                if i != j:
                    soma += matriz_a[i, j] * matriz_x[j]
            temp = matriz_a[i, i]
            matriz_x[i] = (matriz_b[i] - soma) / temp

        if norma(matriz_x, x_anterior) < tol:
            return matriz_x

        k += 1

    raise IteracoesExcedidas


def jacobi(n, coeficiente, coluna, tol, n_max):
    k = 1

    matriz_a = coeficiente.copy()
    matriz_b = coluna.copy()
    matriz_x = matriz_b.copy()

    for i in range(n):
        divisor = matriz_a[i, i] * (-1)
        for j in range(n):
            if i == j:
                matriz_a[i, j] = 0
            else:
                matriz_a[i, j] /= divisor
        matriz_b[i, 0] /= ((-1) * divisor)

    while k < n_max:
        result = matriz_a * matriz_x + matriz_b
        if norma(matriz_x, result) < tol:
            return result

        matriz_x = result
        k += 1

    raise IteracoesExcedidas


def main():
    n = int(input("Insira o número de equações/incógnitas: "))
    print(
        "Escreva a matriz A (coeficientes) de tamanho n x n, separando as colunas por espaço e linhas por parágrafos:")

    coeficientes = []

    for i in range(n):
        numeros = input().split(" ")
        coeficientes.append(numeros)

    matriz = criar_matriz(coeficientes)

    pprint(matriz)

    print("Escreva os valores da matriz coluna B de tamanho n, separados por espaço: ")
    partes = input().split(" ")
    coluna = criar_matriz(partes)

    tol = float(input("Insira a tolerância absoluta: "))
    n_max = int(input("Insira o número máximo de iterações: "))

    try:
        result = gauss_seidel(n, matriz, coluna, tol, n_max)

        def f(element):
            return element.evalf(5)

        pprint(result.applyfunc(f))

    except IteracoesExcedidas:
        print("Número máximo de iterações excedido")


main()
