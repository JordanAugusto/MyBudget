import os
from tkinter import VERTICAL
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
                html.Hr(),
                dbc.Nav(
                [
                    dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                ],  vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}), 
                              
], id="sidebar_completa")





# =========  Callbacks  =========== #
# Pop-up receita
