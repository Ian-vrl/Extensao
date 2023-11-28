# Questão 3
numero = int()
fatorial = 1

print("Digite um número:")
numero = int(input())

for i in range(1, numero + 1):
    fatorial *= i
print("O fatorial de", numero, "é", fatorial)