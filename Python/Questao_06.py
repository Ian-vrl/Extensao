# Verificação de Números Pares e Múltiplos de 3
numero = int()

print("Digite um número inteiro:")
numero = int(input())

if numero % 2 == 0:

    if numero % 3 == 0:
        print("O número é par e múltiplo de 3.")
    else:
        print("O número é par, mas não é múltiplo de 3.")
else:
    print("O número não é par.")