from sympy import *

init_printing(use_unicode=True)


def criar_matriz(elementos):
    matrix_x = [sympify(n) for n in elementos]
    return Matrix(matrix_x)


def jacobi(n, matriz_a, matriz_b, tol, n_max):
    k = 0
    elementos_x = []
    for i in range(n):
        elementos_x.append(0)
    matriz_x = criar_matriz(elementos_x)

    for i in range(n):
        divisor = matriz_a[i, i] * (-1)
        for j in range(n):
            if i == j:
                matriz_a[i, j] = 0
            else:
                matriz_a[i, j] /= divisor
        matriz_b[i, 0] /= ((-1) * divisor)

    while k < n_max:
        matriz_x = matriz_a * matriz_x + matriz_b
         k += 1


def main():
    n = int(input("Insira o número de equações/incógnitas: "))
    print(
        "Escreva a matriz A (coeficientes) de tamanho n x n, separando as colunas por espaço e linhas por parágrafos:")

    coeficientes = []
    valores_b = []

    for i in range(n):
        numeros = input().split(" ")
        coeficientes.append(numeros)

    matriz = criar_matriz(coeficientes)

    print("Escreva os valores da matriz coluna B de tamanho n, separados por espaço: ")
    partes = input().split(" ")
    coluna = criar_matriz(partes)

    tol = input("Insira a tolerância absoluta: ")
    n_max = input("Insira o número máximo de iterações: ")

    jacobi(n, matriz, coluna, tol, n_max)


main()
