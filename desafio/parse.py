import re
from datetime import datetime

from datetime import datetime
from collections import defaultdict

from dash import html, dash_table
import dash_bootstrap_components as dbc

from desafio.database import File
from desafio.config import TRANSACTION_TYPES

regex = r'^(.)(.{8})(.{10})(.{11})(.{12})(.{6})(.{14})(.{18})'

def parse(line):
    match = re.match(regex, line)

    timestamp = datetime.strptime(match.group(2) + match.group(6), '%Y%m%d%H%M%S').timestamp()

    File(transaction=int(match.group(1)), timestamp=timestamp, value=float(match.group(3))/100, cpf=match.group(4), card=match.group(5), store_owner=match.group(7).strip(), store=match.group(8).strip()).save()


def get_base():
    stores = defaultdict(list)
    stores_balance = defaultdict(int)
    for file in File.select():
        stores[file.store].append({
            "Tipo": TRANSACTION_TYPES[file.transaction-1].description,
            "Data": datetime.strftime(file.timestamp, '%Y-%m-%d %H:%M:%S'),
            "Valor": float(file.value), "CPF": file.cpf, "Cartão": file.card 
        })
        stores_balance[file.store] += file.value if TRANSACTION_TYPES[file.transaction-1].income else -file.value

    columns = [{"name": i, "id": i} for i in ["Tipo", "Data", "Valor", "CPF", "Cartão"]]

    accordion = html.Div(
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        dash_table.DataTable(stores[store], columns),
                        dbc.Badge(f"Saldo: {stores_balance[store]}", color="light", text_color="primary", className="ms-1"),
                    ],
                    title=store,
                ) for store in stores
            ]
        )
    )

    return accordion 