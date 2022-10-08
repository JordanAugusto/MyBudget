from logging import PlaceHolder
import os
from tkinter import VERTICAL
from turtle import title
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
                html.H1("Minhas Finanças", className="text-primary"),
                html.P("By Jordan Toledo", className="text-info"),
                html.Hr(),

# criando botoes 
                dbc.Button(id='botao_avatar',
                    children=[html.Img(src='/assets/img_hom.png', alt='Avatar', className='perfil_avatar')
                ], style={'background-color': 'transparent', 'border-color': 'transparent'}),

                dbc.Row([
                    dbc.Col([
                        dbc.Button(color='success', id='open-novo-receita',
                            children=['Receita'])
                    ], width=6),
                    dbc.Col([
                        dbc.Button(color='danger', id='open-novo-despesa',
                            children=['Despesa'])
                    ], width=6)
                ]),
# criando navegaçao do menus
# criando modal receita
                  html.Div([
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Adicionar Receita")),
                        dbc.ModalBody([
                            dbc.Row([
                                dbc.Col([
                                        dbc.Label("Observação: "),
                                        dbc.Input(placeholder="Salario, Pix, Dinheiro...", id="txt-receita"),
                                ], width=6), 
                                dbc.Col([
                                        dbc.Label("Valor: "),
                                        dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                                ], width=6)
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Data: "),
                                    dcc.DatePickerSingle(id='date-receitas',
                                        min_date_allowed=date(2020, 1, 1),
                                        max_date_allowed=date(2030, 12, 31),
                                        date=datetime.today(),
                                        style={"width": "100%"}
                                    ),
                                ], width=4),

                                dbc.Col([
                                    dbc.Label("Situação"),
                                    dbc.Checklist(
                                        options=[{"label": "Foi recebida", "value": 1},
                                            {"label": "Receita Recorrente", "value": 2}],
                                        value=[1],
                                        id="switches-input-receita",
                                        switch=True),
                                ], width=4),

                                dbc.Col([
                                    html.Label("Categoria de Receita"),
                                    dbc.Select(id="select_receita", options=[])
                                ], width=4)
                            ], style={"margin-top": "25px"}),
                            
                            dbc.Row([
                                dbc.Accordion([
                                        dbc.AccordionItem(children=[
                                                dbc.Row([
                                                    dbc.Col([
                                                        html.Legend("Adicionar Categoria", style={'color': 'green'}),
                                                        dbc.Input(type="text", placeholder="Tipo da categoria...", id="input-add-receita", value=""),
                                                        html.Br(),
                                                        dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                                        html.Br(),
                                                        html.Div(id="category-div-add-receita", style={}),
                                                    ], width=6),

                                                    dbc.Col([
                                                        html.Legend("Remover Categoria", style={'color': 'red'}),
                                                        dbc.Checklist(
                                                            id="checklist-selected-style-receita",
                                                            options=[],
                                                            value=[],
                                                            label_checked_style={"color": "red"},
                                                            input_checked_style={"backgroundColor": "#fa7268",
                                                                "borderColor": "#ea6258"},
                                                        ),                                                            
                                                        dbc.Button("Excluir", color="warning", id="remove-category-receita", style={"margin-top": "20px"}),
                                                    ], width=6)
                                                ]),
                                            ], title="Adicionar e Remover Categorias",
                                        ),
                                    ], flush=True, start_collapsed=True, id='accordion-receita'),
                                        
                                        html.Div(id="id_teste_receita", style={"padding-top": "20px"}),
                                    
                                        dbc.ModalFooter([
                                            dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                                            dbc.Popover(dbc.PopoverBody("Registrado!"), target="salvar_receita", placement="left", trigger="click"),
                                            ])
                                ], style={"margin-top": "25px"}),
                            ])
                    ],
                    style={"background-color": "rgba(17, 140, 79, 0.05)"},
                    id="modal-novo-receita",
                    size="lg",
                    is_open=False,
                    centered=True,
                    backdrop=True)
            ]),       
# criando modal despesas
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle("Adicionar Despesa")),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                                dbc.Label("Observação: "),
                                dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-despesa"),
                        ], width=6), 
                        dbc.Col([
                                dbc.Label("Valor: "),
                                dbc.Input(placeholder="$100.00", id="valor_despesa", value="")
                        ], width=6)
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Label("Data: "),
                            dcc.DatePickerSingle(id='date-despesas',
                                min_date_allowed=date(2020, 1, 1),
                                max_date_allowed=date(2030, 12, 31),
                                date=datetime.today(),
                                style={"width": "100%"}
                            ),
                        ], width=4),

                        dbc.Col([
                            dbc.Label("Opções Extras"),
                            dbc.Checklist(
                                options=[{"label": "Foi recebida", "value": 1},
                                    {"label": "despesa Recorrente", "value": 2}],
                                value=[1],
                                id="switches-input-despesa",
                                switch=True),
                        ], width=4),

                        dbc.Col([
                            html.Label("Tipo de despesa"),
                            dbc.Select(id="select_despesa", options=[])
                        ], width=4)
                    ], style={"margin-top": "25px"}),
                    
                    dbc.Row([
                        dbc.Accordion([
                                dbc.AccordionItem(children=[
                                    dbc.Row([
                                        dbc.Col([
                                            html.Legend("Adicionar Categoria", style={'color': 'green'}),
                                            dbc.Input(type="text", placeholder="Tipo da categoria...", id="input-add-despesa", value=""),
                                            html.Br(),
                                            dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                            html.Br(),
                                            html.Div(id="category-div-add-despesa", style={}),
                                        ], width=6),

                                        dbc.Col([
                                            html.Legend("Remover Categoria", style={'color': 'red'}),
                                            dbc.Checklist(
                                                id="checklist-selected-style-despesa",
                                                options=[],
                                                value=[],
                                                label_checked_style={"color": "red"},
                                                input_checked_style={"backgroundColor": "#fa7268",
                                                    "borderColor": "#ea6258"},
                                            ),                                                            
                                            dbc.Button("Excluir", color="warning", id="remove-category-despesa", style={"margin-top": "20px"}),
                                        ], width=6)
                                    ]),
                                ], title="Adicionar e Remover Categorias",
                                ),
                            ], flush=True, start_collapsed=True, id='accordion-despesa'),
                                                    
                        dbc.ModalFooter([
                            dbc.Button("Adicionar Despesa", color="error", id="salvar_despesa", value="despesa"),
                            dbc.Popover(dbc.PopoverBody("Registrado!"), target="salvar_despesa", placement="left", trigger="click"),
                        ]
                        )
                    ], style={"margin-top": "25px"}),
                ])
            ],
            style={"background-color": "rgba(17, 140, 79, 0.05)"},
            id="modal-novo-despesa",
            size="lg",
            is_open=False,
            centered=True,
            backdrop=True),    

#navegaçao do sidebar
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}),
                

], id="sidebar_completa")





# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita','is_open'),
    Input('open-novo-receita','n_clicks'),
    State('modal-novo-receita','is_open'),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa','is_open'),
    Input('open-novo-despesa','n_clicks'),
    State('modal-novo-despesa','is_open'),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open        