from lib.interface import *
from lib.arquivo import *
from time import sleep

nome_arquivo = 'cadastros.txt'

if not arquivoExiste(nome_arquivo):
    criarArquivo(nome_arquivo)

cabeçalho('SISTEMA CADASTRO v1.0')
while True:
    resposta = menu(['Lista de Cadastros', 'Cadastrar Pessoa', 'Sair do Programa'])
    if resposta == 1:
        # Opção de listar pessoas cadastradas
        lerArquivo(nome_arquivo)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(nome_arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[31mERRO. Digite uma opção válida!\033[m')
    sleep(1)
