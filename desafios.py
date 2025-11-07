"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

import re

def mostrar_mensagem_inicial():
    return f'Bem-vindo ao Desafio de Git!'


def listar_comandos_git_basicos():
    comandos = ['git init', 'git add', 'git commit', 'git status', 'git push']
    return f'\n'.join(comandos)


def criar_mensagem_commit(funcao_nome):

    if(funcao_nome == ''):
        return 'Digite o nome da função'

    return f'Implementa função {funcao_nome}'


def verificar_tag_valida(tag):

    padrao = r"^v\d+\.\d+$"
    
    if re.match(padrao, tag):
        return True
    return False


def gerar_relatorio_final(funcoes_concluidas):
    num_funcoes = len(funcoes_concluidas)
    return f"Desafio concluído! {num_funcoes} funções implementadas com sucesso."



