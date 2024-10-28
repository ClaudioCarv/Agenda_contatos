import colorama as color
from time import sleep

#Dicionario
agenda = {}

#titulo
def titulo():
    texto = 'Agenda de contatos'
    largura = 23
    print(f'\n{color.Fore.LIGHTCYAN_EX}{texto.center(largura)}{color.Fore.RESET}')

#cada nome vai estar ligado a um numero
def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"\n{color.Fore.LIGHTGREEN_EX}Contato {nome} adicionado{color.Fore.RESET}")
    sleep(2)

#remover contato do dicionario
def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"\n{color.Fore.RED}Contato {nome} removido{color.Fore.RESET}")
    else:
        print(f"\n{color.Fore.YELLOW}Contato {nome} não encontrado{color.Fore.RESET}")


def buscar_contato(nome):
    if nome in agenda:
        return f"\n{nome}: {agenda[nome]}"
    else:
        return f"\n{color.Fore.YELLOW}Contato {nome} não encontrado{color.Fore.RESET}"

def exibir_contatos():
    if agenda:
        print(f"\n{color.Fore.LIGHTCYAN_EX}Contatos na agenda{color.Fore.RESET}\n")
        for nome, telefone in agenda.items():
            print(f"{color.Fore.LIGHTWHITE_EX}{nome}: {telefone[:5]}-{telefone[4:]}{color.Fore.RESET}")
    else:
        print("A agenda está vazia")

def menu():
    print(f"{color.Fore.BLUE}\nEscolha uma opção abaixo\n{color.Fore.RESET}")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Exibir todos os contatos")
    print("5 - Sair\n")

titulo()
while True:
    menu()
    escolha = input(f"{color.Fore.LIGHTYELLOW_EX}Digite o número de uma das opções:{color.Fore.RESET} ")

    if escolha == '1':
        nome = input(f"{color.Fore.LIGHTYELLOW_EX}Digite o nome do contato:{color.Fore.RESET} ")
        telefone = input(f"{color.Fore.LIGHTYELLOW_EX}Digite o telefone do contato:{color.Fore.RESET} ")
        adicionar_contato(nome, telefone)

    elif escolha == '2':
        nome = input(f"{color.Fore.LIGHTYELLOW_EX}Digite o nome do contato que deseja remover:{color.Fore.RESET} ")
        remover_contato(nome)

    elif escolha == '3':
        nome = input(f"{color.Fore.LIGHTYELLOW_EX}Digite o nome do contato que deseja buscar:{color.Fore.RESET} ")
        print(buscar_contato(nome))

    elif escolha == '4':
        exibir_contatos()
        sleep(3)

    elif escolha == '5':
        print(f"\n{color.Fore.LIGHTRED_EX}Programa Encerrado{color.Fore.RESET}")
        break

    else:
        print(f"\n{color.Fore.RED}Opção inválida{color.Fore.RESET}")
