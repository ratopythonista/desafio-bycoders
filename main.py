import base64

from dash import Dash, dcc, html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from desafio.parse import parse, get_base


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
    html.Div(id='output-cnab-upload', children=html.Div(get_base())),
])

def parse_contents(file):
    _, content_string = file.split(',')

    decoded = base64.b64decode(content_string).decode()

    for line in decoded.splitlines():
        parse(line)

    return get_base()

@app.callback(Output('output-cnab-upload', 'children'),
              Input('upload-cnab', 'contents'),)
def update_output(file):
    if file is not None:
        return parse_contents(file)
    raise PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)