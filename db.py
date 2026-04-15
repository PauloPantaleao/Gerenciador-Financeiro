import sqlite3
class Transacao:
    def __init__(self, desc: str, valor: float, tipo: str):
        if tipo not in ['receita', 'despesa']:
            raise ValueError(f'Tipo "{tipo}" inválido, tente "receita" ou "despesa".')
        if valor <= 0:
            raise ValueError(f'Valor "{valor}" inválido, tem que ser maior que zero.')
        self.id: int | None = None
        self.descricao = desc
        self.valor = valor
        self.tipo = tipo
    def __str__(self):
        return f'[{self.tipo.upper()}] {self.descricao} - R$ {self.valor:.2f}'
    def dados(self):
        return {'id': self.id, 'descricao': self.descricao, 'valor': self.valor, 'tipo': self.tipo}
    def formatado(self):
        return f'{f'id:[{self.id}]':<6}{self.descricao:^22}R${self.valor:>10.2f}'
class GerenciadorFinanceiro:
    def __init__(self, db: str) -> None:
        self.db = db
        self.conexao = sqlite3.connect(db)
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL)''')
        
    def adicionar(self, transacao: Transacao) -> None:
        self.cursor.execute('''
        INSERT INTO transacoes (descricao, valor, tipo) VALUES (?, ?, ?)''', (transacao.descricao, transacao.valor, transacao.tipo))
        transacao.id = self.cursor.lastrowid
        self.conexao.commit()

    def listar(self) -> list[Transacao]:
        self.cursor.execute('''
        SELECT * FROM transacoes''')
        transacoes = self.cursor.fetchall()
        formatado = []
        for t in transacoes:
            forma = Transacao(t[1], t[2], t[3])
            forma.id = t[0]
            formatado.append(forma)
        return formatado
    
    def deletar(self, id: int) -> None:
        self.cursor.execute('''
        DELETE FROM transacoes WHERE id = ?''', (id, ))
        self.conexao.commit()
        
    def saldo(self) -> float:
        return self.receita_total() - self.despesa_total()
    
    def receita_total(self) -> float:
        total = self.cursor.execute('''
        SELECT SUM(valor) FROM transacoes WHERE tipo = "receita"''').fetchone()[0] or 0
        return total
    
    def despesa_total(self) -> float:
        total = self.cursor.execute('''
        SELECT SUM(valor) FROM transacoes WHERE tipo = "despesa"''').fetchone()[0] or 0
        return total

    def fechar(self):
        self.conexao.close()
