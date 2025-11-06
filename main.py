from sympy import *

init_printing(use_unicode=True)


class IteracoesExcedidas(Exception):
    pass


def criar_matriz(elementos):
    matrix = [sympify(n) for n in elementos]
    return Matrix(matrix)


def norma(matriz_a, matriz_b):
    resultado = matriz_b - matriz_a
    return max(resultado, key=abs)


def jacobi(n, coeficiente, coluna, tol, n_max):
    k = 0
    elementos_x = []
    for i in range(n):
        elementos_x.append(0)
    matriz_x = criar_matriz(elementos_x)

    matriz_a = coeficiente
    matriz_b = coluna

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

    print("Escreva os valores da matriz coluna B de tamanho n, separados por espaço: ")
    partes = input().split(" ")
    coluna = criar_matriz(partes)

    tol = float(input("Insira a tolerância absoluta: "))
    n_max = int(input("Insira o número máximo de iterações: "))

    try:
        result = jacobi(n, matriz, coluna, tol, n_max)

        def f(element):
            return element.evalf(5)

        pretty_print(result.applyfunc(f))

    except IteracoesExcedidas:
        print("Número máximo de iterações excedido")


main()
