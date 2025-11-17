# 📐 Solucionador de Sistemas Lineares Iterativo

Um script Python de linha de comando para resolver sistemas de equações lineares da forma $Ax = B$ através de métodos numéricos iterativos.

## ✨ Funcionalidades Principais

  * **Múltiplos Métodos:** Implementa os métodos iterativos de **Gauss-Seidel** e **Gauss-Jacobi** para encontrar o vetor solução $x$.
  * **Escolha do Utilizador:** Permite ao utilizador escolher qual dos dois métodos deseja usar para a resolução.
  * **Verificação de Convergência:** O script analisa a matriz de coeficientes $A$ e verifica duas condições cruciais:
    1.  **Zeros na Diagonal:** Confirma que não existem zeros na diagonal principal, o que impossibilitaria a execução dos métodos.
    2.  **Dominância Diagonal:** Testa se a matriz é *estritamente diagonalmente dominante*. Se for, informa o utilizador que a convergência é garantida; caso contrário, emite um aviso de que a convergência não é garantida.
  * **Tratamento de Erros:** Possui gestão de exceções robusta para lidar com entradas de dimensão incorreta (`DimensoesErradas`), erros de sintaxe na entrada e casos onde o número máximo de iterações é excedido (`IteracoesExcedidas`).
  * **Precisão com SymPy:** Utiliza a biblioteca `SymPy` para lidar com as matrizes e cálculos. Isto permite que o utilizador insira valores simbólicos (como frações, ex: `1/3`) sem perda de precisão imediata.

## 🛠️ Pré-requisitos

Para executar este script, precisa de **Python 3** e da biblioteca **SymPy**.

Pode instalar a dependência usando `pip`:

```bash
pip install sympy
```

## 🚀 Como Usar

1.  Abra um terminal ou linha de comandos.
2.  Navegue até ao diretório onde o ficheiro `main.py` está localizado.
3.  Execute o script:
    ```bash
    python main.py
    ```
4.  O programa irá solicitar, passo a passo:
      * O número de equações/incógnitas ($n$).
      * A matriz de coeficientes $A$ (inserir uma linha de cada vez, com números separados por espaço).
      * O vetor de termos independentes $B$ (inserir todos os valores na mesma linha, separados por espaço).
      * A tolerância absoluta (ex: `0.001`).
      * O número máximo de iterações (ex: `50`).
      * O método desejado (1 para Gauss-Seidel ou 2 para Gauss-Jacobi).

-----

### Exemplo de Execução

Para resolver o sistema (baseado na imagem `image_520301.png`):

$$
\begin{cases}
5x_1 + 1x_2 + 1x_3 = 5 \\
3x_1 + 4x_2 + 1x_3 = 6 \\
3x_1 + 3x_2 + 6x_3 = 0
\end{cases}
$$Com uma tolerância de $\epsilon = 0.05$.

**A entrada e saída no terminal seriam:**

```
*****************************************************************
Bem-vindo ao Solucionador de sistemas lineares (Ax = B)
*****************************************************************

Insira o número de equações/incógnitas: 3

Escreva a matriz A (coeficientes) de tamanho n x n, separando as colunas por espaço e linhas por parágrafos:
5 1 1
3 4 1
3 3 6

Aviso: A matriz inserida não é estritamente diagonalmente dominante!
A convergência para a solução não é garantida

Escreva os valores da matriz coluna B de tamanho n, separados por espaço:
5 6 0

Insira a tolerância absoluta: 0.05
Insira o número máximo de iterações: 50

Escolha o método iterativo:
1) Gauss-Seidel
2) Gauss-Jacobi

Digite o número (1 ou 2): 1

⎧ x1 = 0.77885
| x{i} = 0.88462
⎩ x3 = -0.83173

Deseja continuar? (s/n) n
```
$$
