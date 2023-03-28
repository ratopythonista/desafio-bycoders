from dataclasses import dataclass

@dataclass
class TransactionType:
    number: int
    description: str
    income: bool


TRANSACTION_TYPES = [
    TransactionType(1, 'Débito', True),
    TransactionType(2, 'Boleto', False),
    TransactionType(3, 'Financiamento', False),
    TransactionType(4, 'Crédito', True),
    TransactionType(5, 'Recebimento Empréstimo', True),
    TransactionType(6, 'Vendas', True),
    TransactionType(7, 'Recebimento TED', True),
    TransactionType(8, 'Recebimento DOC', True),
    TransactionType(9, 'Aluguel', False),
]