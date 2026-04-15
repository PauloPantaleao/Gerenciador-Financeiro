import write
from db import Transacao, GerenciadorFinanceiro
from time import sleep
db = GerenciadorFinanceiro('banco.db')
while True:
    write.line()
    write.title('GERENCIADOR FINANCEIRO')
    write.line()
    transacoes = db.listar()
    rendas = [r for r in transacoes if r.tipo == 'receita']
    renda_total = db.receita_total()
    despesas = [d for d in transacoes if d.tipo == 'despesa']
    despesa_total = db.despesa_total()
    saldo = db.saldo()
    print(f'{'Rendas:':<24}R${renda_total:>14.2f}')
    for renda in rendas:
        print(renda.formatado())
    write.line()
    print(f'{'Despesas:':<24}R${despesa_total:>14.2f}')
    for despesa in despesas:
        print(despesa.formatado())
    write.line()
    print(f'{'Saldo:':<24}R${saldo:>14.2f}')
    write.line()
    print('[A] Adicionar  [R] Remover  [X] Sair')
    write.line()
    escolha = ''
    while escolha not in ['A', 'R', 'X']:
        entrada = str(input().strip())
        if entrada:
            escolha = entrada[0].upper()
    sleep(0.5)
    write.line()
    match escolha:
        case 'A':
            tipo = str()
            while tipo not in ['receita', 'despesa']:
                tipo = str(input('Receita ou Despesa?: ').lower())
            desc = str(input('Descrição: '))
            while True:
                try:
                    valor = float(input('Valor: '))
                    break
                except (ValueError, TypeError):
                    print('Valor Inválido!')
            transacao = Transacao(desc, valor, tipo)
            write.line()
            write.title('Adicionando...')
            db.adicionar(transacao)
            sleep(1)
        case 'R':
            while True:
                try:
                    indice = int(input('Digite o id: '))
                    break
                except (ValueError, TypeError):
                    print('Valor inválido!')
            write.line()
            write.title('Removendo...')
            db.deletar(indice)
            sleep(1)
        case 'X':
            write.title('Encerrando aplicação...')
            db.fechar()
            sleep(1)
            break
        case _:
            write.title('ERRO!')
write.line()
write.title('ATÉ A PROXIMA!')
write.line()
