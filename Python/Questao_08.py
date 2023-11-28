# Soma dos Números Pares

def soma_pares(n):
    soma = 0
    for i in range(2, n + 1, 2):
        soma += i
    return soma
n = int(input("Digite um número inteiro positivo:"))
print("A soma dos números pares de 1 até", n, "é", soma_pares(n))