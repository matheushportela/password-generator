"""
TODO Criar um arquivo e guardar a senha que o usuário escolher do prompt, por exemplo: ele escolheu a senha nr 4, é ela que ele vai guardar
TODO Criar um dicionário que o usuario consiga associar a senha que ele escolheu com aquele site específico. Exemplo {Google: abDCasd31@#, Facebook: outrasenha}

! BUG: Se um usuário colocar qualquer coisa que não seja (Yes, y, No, n) na hora de selecionar para regerar a senha, o programa entra em loop infinito

"""
import string
import secrets
import os
import json
import time
from dotenv import load_dotenv


load_dotenv()

ENV_LIST_SYMBOLS = json.loads(os.environ['LIST_SYMBOLS'])
ENV_MENU_CHOICES = json.loads(os.environ['LIST_CHOICES'])

YES_CHOICES = ['yes', 'y']
NO_CHOICES = ['no', 'n']

LIST_USER_PASSWORDS_CHOICES = []

def show_menu():
    while (True):
        print("-----------------------------------------------")
        print("-- 1. Create a Password                      --")
        print("-- 2. test                                   --")
        print("-- 3. Exit                                   --")
        print("-----------------------------------------------")
        choice = int(input("Please, select an option: "))
        if choice in ENV_MENU_CHOICES:
            return choice
        else:
            print("Please select a valid option.\n")

def check_yes_or_no(incomingData):
    while (True):
        if incomingData in YES_CHOICES:
            incomingData = True
            return incomingData
        if incomingData in NO_CHOICES:
            incomingData = False
            return incomingData
        else:
            print("Please select a valid option (Yes / No).\n")

def generate_passwords(length: int, symbols: bool, uppercase: bool):

    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += secrets.choice(ENV_LIST_SYMBOLS)
    if uppercase:
        combination += string.ascii_uppercase

    combinationLength = len(combination)
    newPassword = ""

    for _ in range(length):
        newPassword += combination[secrets.randbelow(combinationLength)]

    return newPassword


def main():
    os.system('cls')
    userChoice = 0
    
    while(userChoice != 3):
        userChoice = show_menu()
        LIST_USER_PASSWORDS_CHOICES.clear()
        match userChoice:
            case 1:
                while(True):
                    try:
                        passLength = int(input("How many characters do you want your password to be? (min: 8, max: 30) "))
                        if passLength < 8 or passLength > 30:
                            print("Please enter a number between 8 and 30 characters.\n")  
                        else:
                            break
                    except ValueError:
                            print("Please input integer only.\n") 

                passSymbols = input("Do you want Symbols in your password? (Yes / No) ").lower()
                passSymbols = check_yes_or_no(passSymbols)

                passUppercase = input("Do you want Uppercase letters in your password? (Yes / No) ").lower()
                passUppercase = check_yes_or_no(passUppercase)

                print("----------------- List of Passwords -----------------")
                for _, index in enumerate(range(5)):
                    generatedPassword = generate_passwords(length=passLength, symbols=passSymbols, uppercase=passUppercase)
                    print(index + 1, ":", generatedPassword)
                    LIST_USER_PASSWORDS_CHOICES.append(generatedPassword)
                print("-----------------------------------------------------")
                
                while(True):
                    regenerateResponse = str(input("Do you want to regenerate the passwords? (Yes / No) ")).lower()
                    regenerateResponse = check_yes_or_no(regenerateResponse)
                    print(regenerateResponse)
                    
                    if(regenerateResponse):
                        os.system('cls')
                        LIST_USER_PASSWORDS_CHOICES.clear()
                        
                        print("----------------- List of Passwords -----------------")
                        for _, index in enumerate(range(5)):
                            generatedPassword = generate_passwords(length=passLength, symbols=passSymbols, uppercase=passUppercase)
                            print(index + 1,":", generatedPassword)
                            LIST_USER_PASSWORDS_CHOICES.append(generatedPassword)
                        print("-----------------------------------------------------")
                    else:
                        os.system('cls')
                        print("----------------- List of Passwords -----------------")
                        for index, value in enumerate(LIST_USER_PASSWORDS_CHOICES):      
                            print(index + 1,":", value)
                        print("-----------------------------------------------------")
                        
                        while(True):
                            savedPassword = int(input("Which password do you want to save? (1, 2, 3, 4 or 5)\n"))
                            
                            if(savedPassword > 0 and savedPassword <= len(LIST_USER_PASSWORDS_CHOICES)):
                                savedPassword = LIST_USER_PASSWORDS_CHOICES[savedPassword - 1]
                                os.system('cls')
                                print(f"You selected this password: {savedPassword}")
                                print("Saving to your system...\n\n")
                                time.sleep(3)
                                break
                            else:
                                print("Please select a valid option.\n")
                        break
            case 2:
                print("Not implemented yet")
            case 3:
                print("Exiting...")
                time.sleep(3)
                os.system('cls')
            case _:
                print("Please select a valid option (1, 2, 3).\n")


if __name__ == "__main__":
    main()
