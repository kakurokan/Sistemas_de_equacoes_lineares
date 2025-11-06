from sympy import *

init_printing(use_unicode=True)


def main():
    n = int(input("Insira o número de equações/incógnitas: "))
    print(
        "Escreva a matriz A (coeficientes) de tamanho n x n, separando as colunas por espaço e linhas por parágrafos:\n")

    matriz = []
    valores_b = []

    for i in range(n):
        numeros = input().split(" ")
        numeros_sympy = [sympify(elemento) for elemento in numeros]
        matriz.append(numeros_sympy)

    linha = input("Escreva os valores da matriz coluna B de tamanho n, separados por espaço")
    partes = linha.split(" ")
    for i in partes:
        valores_b.append(sympify(i))

    tol = input("Insira a tolerância absoluta: ")
    n_max = input("Insira o número máximo de iterações: ")


main()
