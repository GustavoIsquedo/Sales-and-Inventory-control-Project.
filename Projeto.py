# UNIVERSIDADE DE MOGI DAS CRUZES -  UMC
# GUSTAVO GALVÃO, LUCAS CAVALCANTE E LUCAS RODRIGUES
# TRABALHO AVALIATIVO DE SOFTWARE BÁSICO
 
import os
import re
from colorama import Fore, Style, init
from tabulate import tabulate
 
init(autoreset=True)
 
# Título do sistema
TITULO_INICIO = Fore. CYAN + Style.BRIGHT + '''
██████╗ ███████╗███╗   ███╗    ██╗   ██╗██╗███╗   ██╗██████╗  ██████╗
██╔══██╗██╔════╝████╗ ████║    ██║   ██║██║████╗  ██║██╔══██╗██╔═══██╗
██████╔╝█████╗  ██╔████╔██║    ██║   ██║██║██╔██╗ ██║██║  ██║██║   ██║
██╔══██╗██╔══╝  ██║╚██╔╝██║    ╚██╗ ██╔╝██║██║╚██╗██║██║  ██║██║   ██║
██████╔╝███████╗██║ ╚═╝ ██║     ╚████╔╝ ██║██║ ╚████║██████╔╝╚██████╔╝
╚═════╝ ╚══════╝╚═╝     ╚═╝      ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝'''
 
TITULO = Fore. CYAN + Style.BRIGHT + '''
███████╗███████╗████████╗ ██████╗  ██████╗ ██╗   ██╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║   ██║██╔════╝
█████╗  ███████╗   ██║   ██║   ██║██║   ██║██║   ██║█████╗  
██╔══╝  ╚════██║   ██║   ██║   ██║██║▄▄ ██║██║   ██║██╔══╝  
███████╗███████║   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝'''
 
TITULO_ADICIONANDO = Fore. CYAN + Style.BRIGHT + '''
 █████╗ ██████╗ ██╗ ██████╗██╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗██████╗  ██████╗     ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗████████╗ ██████╗
██╔══██╗██╔══██╗██║██╔════╝██║██╔═══██╗████╗  ██║██╔══██╗████╗  ██║██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
███████║██║  ██║██║██║     ██║██║   ██║██╔██╗ ██║███████║██╔██╗ ██║██║  ██║██║   ██║    ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║   ██║   ██║   ██║
██╔══██║██║  ██║██║██║     ██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║██║  ██║██║   ██║    ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║   ██║   ██║   ██║
██║  ██║██████╔╝██║╚██████╗██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║██████╔╝╚██████╔╝    ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║   ╚██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ '''
 
TITULO_ATUALIZANDO = Fore. CYAN + Style.BRIGHT + '''
 █████╗ ████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ███╗   ██╗██████╗  ██████╗              
██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗████╗  ██║██╔══██╗██╔═══██╗            
███████║   ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██╔██╗ ██║██║  ██║██║   ██║            
██╔══██║   ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██║╚██╗██║██║  ██║██║   ██║            
██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║██║ ╚████║██████╔╝╚██████╔╝    ██╗██╗██╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝     ╚═╝╚═╝╚═╝
                                                                                                     '''
 
 
TITULO_REMOVENDO = Fore. CYAN + Style.BRIGHT + '''
██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗██████╗  ██████╗              
██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝████╗  ██║██╔══██╗██╔═══██╗            
██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║   ██║            
██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║   ██║            
██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗██║ ╚████║██████╔╝╚██████╔╝    ██╗██╗██╗
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝     ╚═╝╚═╝╚═╝'''
 
TITULO_PESQUISA = Fore. CYAN + Style.BRIGHT + '''
██████╗ ███████╗███████╗ ██████╗ ██╗   ██╗██╗███████╗ █████╗     ██████╗  █████╗ ██████╗  ██████╗██╗ █████╗ ██╗        
██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██║        
██████╔╝█████╗  ███████╗██║   ██║██║   ██║██║███████╗███████║    ██████╔╝███████║██████╔╝██║     ██║███████║██║        
██╔═══╝ ██╔══╝  ╚════██║██║▄▄ ██║██║   ██║██║╚════██║██╔══██║    ██╔═══╝ ██╔══██║██╔══██╗██║     ██║██╔══██║██║        
██║     ███████╗███████║╚██████╔╝╚██████╔╝██║███████║██║  ██║    ██║     ██║  ██║██║  ██║╚██████╗██║██║  ██║███████╗    
╚═╝     ╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    
                                                                                                                       
                      ██████╗  ██████╗ ██████╗     ███╗   ██╗ ██████╗ ███╗   ███╗███████╗                              
                      ██╔══██╗██╔═══██╗██╔══██╗    ████╗  ██║██╔═══██╗████╗ ████║██╔════╝                              
                      ██████╔╝██║   ██║██████╔╝    ██╔██╗ ██║██║   ██║██╔████╔██║█████╗                                
                      ██╔═══╝ ██║   ██║██╔══██╗    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝                                
                      ██║     ╚██████╔╝██║  ██║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗                              
                      ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                               '''
 
 
ARQUIVO = "estoque.txt"
 
HEADERS = [
    Fore.BLUE + Style.BRIGHT + "ID" + Style.RESET_ALL,
    Fore.BLUE + Style.BRIGHT + "Categoria" + Style.RESET_ALL,
    Fore.BLUE + Style.BRIGHT + "Nome" + Style.RESET_ALL,
    Fore.BLUE + Style.BRIGHT + "Quantidade" + Style.RESET_ALL,
    Fore.BLUE + Style.BRIGHT + "Preço" + Style.RESET_ALL
]
 
# Funções utilitárias
def msg_erro(msg):
    print(f"{Fore.RED}[ERRO] {msg}{Style.RESET_ALL}")
 
def msg_sucesso(msg):
    print(f"{Fore.GREEN}[SUCESSO] {msg}{Style.RESET_ALL}")
 
def pausar():
    input("\nPressione ENTER para continuar...")
 
def validar_id(id):
    return re.fullmatch(r"[0-9_]+", id) is not None
 
# Operações de arquivo
def verificar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8"):
            pass
 
def carregar_dados():
    verificar_arquivo()
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    produtos = []
    for linha in linhas:
        partes = linha.strip().split(";")
        if len(partes) == 5:
            produtos.append({
                "id": partes[0],
                "categoria": partes[1],
                "nome": partes[2],
                "quantidade": int(partes[3]),
                "preco": float(partes[4])
            })
    return produtos
 
def salvar_dados(produtos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p['id']};{p['categoria']};{p['nome']};{p['quantidade']};{p['preco']}\n")
 
def formatar_quantidade(quantidade):
    cor = Fore.RED if quantidade <= 5 else Fore.GREEN
    return f"{cor}{quantidade}{Style.RESET_ALL}"
 
def exibir_tabela(produtos):
    tabela = []
    for p in produtos:
        tabela.append([
            p['id'],
            p['categoria'],
            p['nome'],
            formatar_quantidade(p['quantidade']),
            f"{Fore.WHITE}R$ {Style.RESET_ALL}{Fore.GREEN}{p['preco']:.2f}{Style.RESET_ALL}"
        ])
    print(tabulate(tabela, headers=HEADERS, tablefmt="fancy_grid", stralign="center", numalign="right"))
 
def exibir_cabecalho():
    print (TITULO_INICIO)
    print(Fore.CYAN + Style.NORMAL + "       ╔══════════════════════════════════════════════╗")
    print(Fore.CYAN + Style.NORMAL + "       ║      SISTEMA DE CONTROLE DE SUPLEMENTOS      ║")
    print(Fore.CYAN + Style.NORMAL + "       ╚══════════════════════════════════════════════╝\n")
 
# Operações principais
def adicionar_produto():
    print(TITULO_ADICIONANDO)
    produtos = carregar_dados()
    print("\nDigite 'v' para voltar a qualquer momento.\n")
 
    id = input("ID do produto (Único, sem espaços ou caracteres especiais): ").strip()
    if id.lower() == 'v':
        return
    if not validar_id(id):
        msg_erro("ID inválido! Use apenas números e underline.")
        pausar()
        return
    if any(p['id'] == id for p in produtos):
        msg_erro("ID já cadastrado. Inclusão não realizada.")
    else:
        categoria = input("Categoria: ").strip()
        if categoria.lower() == 'v':
            return
 
        nome = input("Nome do Produto: ").strip()
        if nome.lower() == 'v':
            return
 
        while True:
            quantidade_str = input("Quantidade: ").strip()
            if quantidade_str.lower() == 'v':
                return
            if quantidade_str.isdigit():
                quantidade = int(quantidade_str)
                break
            else:
                msg_erro("Digite um número válido para quantidade.")
 
        while True:
            preco_str = input("Preço: ").strip()
            if preco_str.lower() == 'v':
                return
            try:
                preco = float(preco_str)
                break
            except ValueError:
                msg_erro("Digite um valor válido para o preço.")
 
        novo = {
            "id": id,
            "categoria": categoria,
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }
        produtos.append(novo)
        salvar_dados(produtos)
        msg_sucesso("Produto incluído com sucesso!")
 
    pausar()
 
def atualizar_produto():
    print(TITULO_ATUALIZANDO)
    produtos = carregar_dados()
    print("\nDigite 'v' para voltar a qualquer momento.\n")
    id = input("Informe o ID do produto que deseja alterar: ").strip()
    if id.lower() == 'v':
        return
    if not validar_id(id):
        msg_erro("ID inválido! Use apenas letras, números e underline.")
        pausar()
        return
 
    for p in produtos:
        if p["id"] == id:
            print(Fore.CYAN + Style.BRIGHT + "Produto encontrado:" + Style.RESET_ALL)
            (f"""
Produto encontrado:
  ID: {p['id']}
  Categoria: {p['categoria']}
  Nome: {p['nome']}
  Quantidade: {p['quantidade']}
  Preço: R$ {p['preco']}
""")
            categoria = input(f"Nova Categoria ({p['categoria']}): ").strip()
            if categoria.lower() == 'v':
                return
            p["categoria"] = categoria or p["categoria"]
 
            nome = input(f"Novo Nome ({p['nome']}): ").strip()
            if nome.lower() == 'v':
                return
            p["nome"] = nome or p["nome"]
 
            while True:
                quantidade = input(f"Nova Quantidade ({p['quantidade']}): ").strip()
                if quantidade.lower() == 'v':
                    return
                if not quantidade:
                    break
                if quantidade.isdigit():
                    p["quantidade"] = int(quantidade)
                    break
                else:
                    msg_erro("Digite um número válido para quantidade.")
 
            while True:
                preco = input(f"Novo Preço ({p['preco']}): ").strip()
                if preco.lower() == 'v':
                    return
                if not preco:
                    break
                try:
                    p["preco"] = float(preco)
                    break
                except ValueError:
                    msg_erro("Digite um valor válido para o preço.")
 
            salvar_dados(produtos)
            msg_sucesso("Produto alterado com sucesso!")
            break
    else:
        msg_erro("Produto não encontrado.")
 
    pausar()
 
def remover_produto():
    print(TITULO_REMOVENDO)
    produtos = carregar_dados()
    print("\nDigite 'v' para voltar a qualquer momento.\n")
    id = input("Informe o ID do produto que deseja excluir: ").strip()
    if id.lower() == 'v':
        return
 
    novos_produtos = [p for p in produtos if p["id"] != id]
    if len(novos_produtos) == len(produtos):
        msg_erro("Produto não encontrado.")
    else:
        salvar_dados(novos_produtos)
        msg_sucesso("Produto excluído com sucesso!")
 
    pausar()
 
def relatorio_produto():
    print(TITULO)
    produtos = carregar_dados()
    if not produtos:
        msg_erro("Nenhum produto cadastrado.")
    else:
        exibir_tabela(produtos)
    pausar()
 
def consultar_produto():
    print(TITULO_PESQUISA)
    produtos = carregar_dados()
    print("\nDigite 'v' para voltar a qualquer momento.\n")
    termo = input("Digite parte do nome para pesquisar: ").lower().strip()
    if termo == 'v':
        return
 
    encontrados = [p for p in produtos if termo in p["nome"].lower()]
    if not encontrados:
        msg_erro("Nenhum produto encontrado.")
    else:
        exibir_tabela(encontrados)
    pausar()
 
# Interface do sistema
def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        exibir_cabecalho()
        print(f"{Fore.GREEN}{Style.BRIGHT}1{Style.RESET_ALL} - {Fore.WHITE}Adicionar Produto")
        print(f"{Fore.GREEN}{Style.BRIGHT}2{Style.RESET_ALL} - {Fore.WHITE}Atualizar Produto")
        print(f"{Fore.GREEN}{Style.BRIGHT}3{Style.RESET_ALL} - {Fore.WHITE}Remover Produto")
        print(f"{Fore.GREEN}{Style.BRIGHT}4{Style.RESET_ALL} - {Fore.WHITE}Relatório de Produtos")
        print(f"{Fore.GREEN}{Style.BRIGHT}5{Style.RESET_ALL} - {Fore.WHITE}Consultar Produto")
        print(f"{Fore.GREEN}{Style.BRIGHT}6{Style.RESET_ALL} - {Fore.WHITE}Sair\n")
 
        opcao = input(Fore.GREEN + Style.BRIGHT + "Escolha uma opção: " + Style.RESET_ALL).strip()
        os.system("cls" if os.name == "nt" else "clear")
 
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            relatorio_produto()
        elif opcao == "5":
            consultar_produto()
        elif opcao == "6":
            print(Fore.MAGENTA + "Saindo do sistema..." + Style.RESET_ALL)
            break
        else:
            msg_erro("Opção inválida.")
            pausar()
 
# Execução
if __name__ == "__main__":
    print(TITULO)
    menu()