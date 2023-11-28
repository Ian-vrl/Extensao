# Questao 5
altura = float(input("Digite sua altura (em metros):"))
peso = float(input("Digite seu peso (em quilogramas):"))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
    print("Você está abaixo do peso. Seu IMC é", imc, "e você está classificado como", categoria)
elif imc < 25:
    categoria = "Peso normal"
    print("Você está com peso normal. Seu IMC é", imc, "e você está classificado como", categoria)
elif imc < 30:
    categoria = "Sobrepeso"
    print("Você está com sobrepeso. Seu IMC é", imc, "e você está classificado como", categoria)
elif imc < 35:
    categoria = "Obesidade grau I"
    print("Você está com obesidade grau I. Seu IMC é", imc, "e você está classificado como", categoria)
elif imc < 40:
    categoria = "Obesidade grau II"
    print("Você está com obesidade grau II. Seu IMC é", imc, "e você está classificado como", categoria)
else:
    categoria = "Obesidade grau III"
    print("Você está com obesidade grau III. Seu IMC é", imc, "e você está classificado como", categoria)
