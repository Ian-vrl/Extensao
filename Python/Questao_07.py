# Validando Senha Forte
def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not any(c.isupper() for c in senha):
        return False
    if not any(c.isdigit() for c in senha):
        return False
    if not any(c in ["@", "#", "!"] for c in senha):
        return False
    return True

print("Sua senha deve conter:")
print("Pelo menos 8 caracteres de comprimento.")
print("Uma letra maiúscula.")
print("Um número.")
print("Um caractere especial, como @, #, ou !.")
senha = input("Digite uma senha:")

if valida_senha(senha):
    print("A senha atende a todos os critérios.")
else:
    print("A senha não atende a todos os critérios.")