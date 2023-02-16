"""
TODO Criar um menu onde o usuário consiga escolher o tamanho e o tipo de senha que ele quer criar, se ele quer com simbolos ou com uppercase
TODO Criar um arquivo e guardar a senha que o usuário escolher do prompt, por exemplo: ele escolheu a senha nr 4, é ela que ele vai guardar
TODO Criar um dicionário que o usuario consiga associar a senha que ele escolheu com aquele site específico. Exemplo {Google: abDCasd31@#, Facebook: outrasenha}

"""
import string
import secrets

SYMBOLS = ['!', "@", "#", "$", "%", "&", "*"]


def generate_password(length: int, symbols: bool, uppercase: bool):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += secrets.choice(SYMBOLS)

    if uppercase:
        combination += string.ascii_uppercase

    combinationLength = len(combination)

    newPassword = ""

    for _ in range(length):
        newPassword += combination[secrets.randbelow(combinationLength)]

    return newPassword


for _, index in enumerate(range(5)):
    print(index + 1, ":", generate_password(length=20, symbols=True, uppercase=True))
