from sympy import *


class IteracoesExcedidas(Exception):
    pass


class DimensoesErradas(Exception):
    pass


def verifica_matriz(matriz, n):
    for i in range(n):
        if matriz[i, i] == 0:
            return false
    return true


def escolha_metodo():
    while True:
        print("Escolha o método iterativo:\n",
              "1) Gauss-Seidel\n",
              "2) Gauss-Jacobi\n")
        escolha = input("Digite o número (1 ou 2): ").strip()
        if escolha == "1":
            return "S"
        elif escolha == "2":
            return "J"
        else:
            print("\nErro: Entrada inválida. Por favor, digite apenas 1 ou 2.\n")


def criar_matriz(elementos):
    matrix = [sympify(n) for n in elementos]
    return Matrix(matrix)


def norma(matriz_a, matriz_b):
    resultado = matriz_b - matriz_a
    return max(resultado, key=abs)


def seidel(n, coeficiente, coluna, tol, n_max):
    k = 0
    elementos_x = [0] * n
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
    print("*" * 65)
    print("   Bem-vindo ao Solucionador de sistemas lineares (Ax = B)")
    print("*" * 65)
    print("")

    n = 0
    rodando = true

    while rodando:
        try:
            n = int(input("Insira o número de equações/incógnitas: "))
            if n <= 0:
                raise ValueError("Número inválido")

            print(
                "Escreva a matriz A (coeficientes) de tamanho n x n, separando as colunas por espaço e linhas por parágrafos:")
            coeficientes = []

            for i in range(n):
                numeros = input().split(" ")
                tamanho = len(numeros)
                if tamanho > n or tamanho < n:  # Caso o utilizador tente inserir mais que n números na linha
                    raise DimensoesErradas
                coeficientes.append(numeros)

            matriz = criar_matriz(coeficientes)
            if not verifica_matriz(matriz, n):
                print("\nErro: Pelo menos um elemento na diagonal principal é ZERO.",
                      "\nOs métodos de Jacobi e Gauss-Seidel não podem ser",
                      "executados, pois ambos exigem que a matriz seja invertível",
                      "\nPor favor, verifique a sua matriz A e tente novamente.\n")
                continue

            print("Escreva os valores da matriz coluna B de tamanho n, separados por espaço: ")
            partes = input().split(" ")
            tamanho = len(partes)
            if tamanho > n or tamanho < n:  # Caso o utilizador tente inserir mais que n números na linha
                raise DimensoesErradas
            coluna = criar_matriz(partes)

            tol = float(input("Insira a tolerância absoluta: "))
            n_max = int(input("Insira o número máximo de iterações: "))
            if n_max <= 0:
                raise ValueError("Erro: Número inválido\n")

            escolha = escolha_metodo()
            if escolha == "J":
                result = jacobi(n, matriz, coluna, tol, n_max)
            else:
                result = seidel(n, matriz, coluna, tol, n_max)

            def f(element):  # Função que arredonda todos os valores da matriz para 5 casas decimais
                return element.evalf(5)

            pprint(result.applyfunc(f))

            rodando = input("Deseja continuar? (s/n) ").strip().lower() == "s"

        except IteracoesExcedidas:
            print("Erro: Número máximo de iterações excedido\n")
        except DimensoesErradas:
            print(f"Erro: A linha inserida não condiz com a dimensão fornecida. Tente novamente\n")
        except SympifyError as e:
            print(f"Erro de sintaxe: {e}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"Erro inesperado: {e}")


main()
