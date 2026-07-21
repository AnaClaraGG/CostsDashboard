from dash import Dash, dcc, html
from . import ids

def render(app:Dash) -> html.Div:
    all_nations = ["South Korea", "United States", "Japan", "Germany", "France", "Italy", "United Kingdom", "Canada", "Australia", "Brazil "]
    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                options=[{"label": nation, "value": nation} for nation in all_nations],
                value=all_nations,
                multi=True,
            ),
            html.Button(
                className="dorpdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_NATIONS_BUTTON,
            )
        ]
    )