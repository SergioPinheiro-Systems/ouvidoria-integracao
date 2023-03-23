from operacoesbd import *

import os
import platform

def limpar():
       if platform.system() == 'Windows':
            os.system('cls')
       if platform.system() == 'Linux':
            os.system('clear')

opcao = 10
conexao = abrirBancoDados('localhost','root','!Smcp1205','ouvidoria')

while opcao != '5':
    print('╔========================================╗')
    print('║      UNIVERSIDADE ABELLA SYSTEMS       ║')
    print('╠========================================╣')
    print('║             MENU OUVIDORIA             ║')
    print('╠========================================╣')
    print('║1) Listar as reclamações.               ║')
    print('║2) Adicionar nova reclamação.           ║')
    print('║3) Remover uma reclamação.              ║')
    print('║4) Pesquisar uma reclamação por código. ║')
    print('║5) Sair do Sistema.                     ║')
    print('╚=═======================================╝')
    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        limpar()
        consultaListagem = 'select * from solicitacao'
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)
        if len(listaReclamacoes) == 0:
            print('Não Existem Reclamações!')
            input('Aperte "Enter" para voltar nas opções. ')
            limpar()

        else:
            print('==========================================')
            print('           LISTA DAS RECLAMAÇÕES          ')
            print('==========================================')
            for solicitacao in listaReclamacoes:
                print('Código:', solicitacao[0],'- Reclamação:', solicitacao[1])
                #print()
            input('Aperte "Enter" para voltar nas opções. ')
            limpar()

    elif opcao == 2:

        limpar()
        novaReclamacao = input('Por Favor, Digite Sua Reclamação, em Seguida, Aperte "Enter": ')

        if novaReclamacao == ' ' or len(novaReclamacao) <= 10:
            print()
            print('Descrição Inválida. Por Favor, Digite Um Texto Valido Sobre a Sua Reclamação.')
            print()
            input('Para Voltar ao Menu Principal Aperte "Enter". ')
            limpar()

        else:
            consultaNovaReclamacao = 'insert into solicitacao(reclamacao) values(%s)'
            dados = (novaReclamacao,)
            insertNoBancoDados(conexao, consultaNovaReclamacao, dados)
            print("")
            print('Reclamação Cadastrada com Sucesso  .')
            print("")
            input('Para Voltar ao Menu Principal Aperte "Enter".  ')
            limpar()

    limpar()
    consultaListagem = 'select * from solicitacao'
    listaReclamacoes = listarBancoDados(conexao, consultaListagem)
    if len(listaReclamacoes) == 0:
        print('Não Existem Reclamações!')
        input('Aperte "Enter" para voltar nas opções. ')
        limpar()

    elif opcao == 3:
        limpar()
        consultaListagem = 'select * from solicitacao'
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Não Existe Reclaçãoes Cadastradas no Sistema.')
            input('Aperte "Enter" para voltar nas opções. ')
            limpar()

        else:
            print('==========================================')
            print('           LISTA DAS RECLAMAÇÕES          ')
            print('==========================================')

            for solicitacao in listaReclamacoes:
                print('Código:', solicitacao[0], '- Reclamação:', solicitacao[1])

        codigoRemover = input('Digite o Código da Reclamação que Deseja Remover? ')

        try:
            codigoRemoverInt = int(codigoRemover)

        except:
            print()
            print('Código inválido. Por favor, digite apenas número de acordo com a listagem!')
            print()
            input('Aperte "Enter" para voltar nas opções. ')
            limpar()

        else:
            if codigoRemoverInt <= 0 or codigoRemoverInt > len(listaReclamacoes):
             print()
             print('Código inválido. Por favor, digite apenas número de acordo com a listagem!')
             print()
             input('Aperte "Enter" para voltar nas opções. ')
             limpar()

            else:

                consultaRemoverReclamacao = 'delete from solicitacao where codigo = %s'
                dados = (codigoRemover,)
                excluirBancoDados(conexao, consultaRemoverReclamacao, dados)
                print('Reclamação Excluida com Sucesso!')
                print()
                input('Aperte "Enter" para voltar nas opções. ')
                limpar()

    elif opcao == 4:
        limpar()
        consultaListagem = 'select * from solicitacao'
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Não Existe Reclaçãoes Cadastradas no Sistema.')
            input('Aperte "Enter" para voltar nas opções. ')
            limpar()
        else:
            print('==========================================')
            print('           LISTA DAS RECLAMAÇÕES          ')
            print('==========================================')

            for solicitacao in listaReclamacoes:
                print('Código:', solicitacao[0], '- Reclamação:', solicitacao[1])

        print()
        print('Pesquisa Reclamações por Codigo')
        codigo = input('Digite o Código da Reclamação a Ser Pesquisada ')
        consultaListagem = 'select * from solicitacao where codigo = ' + codigo
        listaReclamacoes = listarBancoDados(conexao, consultaListagem)

        if len(listaReclamacoes) == 0:
            print('Não Existem Reclamações!')
        else:
            print()
            print('Abaixo a Reclamação Selecionada:')
            for solicitacao in listaReclamacoes:
             print('Código:', solicitacao[0], '- Reclamação:', solicitacao[1])
            print('Sua Solicitação está sendo avaliada e em breve retornaremos')
            print()
        input('Aperte "Enter" para voltar nas opções. ')
        limpar()

    elif opcao == 5:
                limpar()
                print("")
                print('Muito obrigado por usar o Sistema Ouvidoria. Até logo!')
                print("")
                break

encerrarBancoDados(conexao)

