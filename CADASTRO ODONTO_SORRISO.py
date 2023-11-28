# Colocar Loop na tela de login #
# Colocar em nome em especifico caracteres de letras
# email colocar com @gmail.com #
# Adicionar lista de planos para usuário (Array de 10 números)
import os
import sys
from datetime import datetime

def pausar_execucao():
    input("Pressione Enter para continuar...")

def validar_email(email):
    # Verifica se o e-mail contém pelo menos um "@" (símbolo típico em um e-mail)
    if "@" not in email:
        return False

    # Divide o e-mail em nome de usuário e domínio
    nome_usuario, dominio = email.split("@")

    # Verifica se o domínio tem pelo menos 3 caracteres e após o "@" existe pelo menos 1 caractere
    return len(dominio) >= 3 and len(nome_usuario) >= 3
# Exemplo de uso:
email_valido = validar_email("usuario@dominio.com")
print(email_valido)  # Isso imprimirá True se o e-mail for válido, False caso contrário

def validar_telefone(telefone):
    # Verifica se o número de telefone tem o formato de DDD com dois dígitos
    return telefone.isdigit() and len(telefone) >= 10  # Aqui consideramos que o DDD tem dois dígitos e o número tem pelo menos 8 dígitos

def Cadastro():
    # Início da criação de variáveis e strings
    arquivo = ""
    
    # Solicitar o CPF até que seja fornecido um com 11 dígitos
    while True:
        CPF = input("Digite o CPF a ser cadastrado (11 dígitos):\n")
        if len(CPF) == 11 and CPF.isdigit():
            break
        else:
            print("CPF inválido. Certifique-se de fornecer um CPF válido!.")

    arquivo = CPF

    while True:
        nome = input("Digite o nome que gostaria de cadastrar:\n")
        if nome.strip():  # Verifica se o nome não está vazio
            break
        else:
            print("Nome inválido. Por favor, forneça um nome.")

    while True:
        sobrenome = input("Digite o Sobrenome que gostaria de cadastrar:\n")
        if sobrenome.strip():  # Verifica se o sobrenome não está vazio
            break
        else:
            print("Sobrenome inválido. Por favor, forneça um sobrenome.")

    # Solicitar a data de nascimento até que seja fornecida uma data válida
    while True:
        try:
            data_nascimento_str = input("Digite a data de nascimento (formato: DD/MM/AAAA):\n")
            data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Data de nascimento inválida. Certifique-se de usar o formato DD/MM/AAAA.")

    # Solicitar o e-mail até que seja fornecido um válido
    while True:
        email = input("Digite o e-mail:\n")
        if validar_email(email):
            break
        else:
            print("E-mail inválido. Certifique-se de incluir um endereço de email válido.")

    # Solicitar o número de telefone até que seja fornecido um válido
    while True:
        telefone = input("Digite o número de telefone (com DDD):\n")
        if validar_telefone(telefone):
            break
        else:
            print("Número de telefone inválido. Certifique-se de incluir o DDD com dois dígitos.")

    # Solicitar o plano até que seja fornecido um válido
    opcoes_plano = ["Mensal", "Anual", "Premium"]
    while True:
        plano = input("Digite o plano que o Usuário assinou (Mensal, Anual ou Premium):\n").capitalize()
        if plano in opcoes_plano:
            break
        else:
            print("Plano inválido. Escolha entre Mensal, Anual ou Premium.")

    with open(arquivo, "w") as file:
        file.write(f"{CPF}\n")
        file.write(f"{nome}\n")
        file.write(f"{sobrenome}\n")
        file.write(f"{data_nascimento.strftime('%d/%m/%Y')}\n")  # Salva a data de nascimento no formato DD/MM/AAAA
        file.write(f"{email}\n")
        file.write(f"{telefone}\n")
        file.write(f"{plano}\n")

        print("\n Usuário cadastrado com sucesso ! \n")

    pausar_execucao()

def Consulta():
    CPF = input("Digite o CPF da pessoa que gostaria de consultar:\n")

    try:
        with open(CPF, "r") as file:
            print("\nEsses são os dados do usuário:\n")
            for linha in file:
                print(linha.strip())  # Remove espaços em branco no início e no final da linha
    except FileNotFoundError:
        print(f"Usuário com CPF {CPF} não encontrado!")

    pausar_execucao()

def Retirar():
    CPF = input("Qual o CPF do usuário que gostaria de retirar ?:\n")

    try:
        os.remove(CPF)
        print("Usuário removido com sucesso!")
    except FileNotFoundError:
        print(f"Usuário com CPF {CPF} não encontrado!")
    except Exception as e:
        print(f"Não foi possível remover o usuário. Erro: {e}")

    pausar_execucao()

def Sair():
    print("Obrigado, até logo!")
    sys.exit(0)
    pausar_execucao()

def opcao_invalida():
    print("Opção inválida. Selecione uma das opções acima!")
    pausar_execucao()

def main():
    opcoes = {
        1: Cadastro,
        2: Consulta,
        3: Retirar,
        4: Sair
    }

    menu_opcoes = "\n".join([f"\t{i} - {opcao.__name__}" for i, opcao in opcoes.items()])

    senha_digitada = input("### Cadastro ODONTO SORRISO ### \n\nLogin de Administrador\n\nDigite a sua senha:")

    if senha_digitada == "admin":
        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print("### Cadastro ODONTO SORRISO ### \n\n")
            print("Escolha as opções do menu: \n\n")
            print(menu_opcoes)

            try:
                opcao = int(input("Opção: "))
                os.system("cls" if os.name == "nt" else "clear")

                opcoes.get(opcao, opcao_invalida)()

            except ValueError:
                print("Por favor, insira um número válido.")
                pausar_execucao()

if __name__ == "__main__":
    main()
