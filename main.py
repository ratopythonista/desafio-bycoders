import base64

from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Upload(
        id='upload-cnab',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-cnab-upload'),
])

def parse_contents(file):
    content_type, content_string = file.split(',')

    decoded = base64.b64decode(content_string).decode()

    table_header = [
        html.Thead(html.Tr([html.Th("Conteudo")]))
    ]

    rows = list()
    for line in decoded.splitlines():
        row = html.Tr([html.Td(line)])
        rows.append(row)

    table_body = [html.Tbody(rows)]

    table = dbc.Table(table_header + table_body, bordered=True)

    return table

@app.callback(Output('output-cnab-upload', 'children'),
              Input('upload-cnab', 'contents'),)
def update_output(file):
    if file is not None:
        return parse_contents(file)

if __name__ == '__main__':
    app.run_server(debug=True)