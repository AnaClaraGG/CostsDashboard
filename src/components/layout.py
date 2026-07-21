from dash import Dash, html
from . import nation_dropdown, bar_chart

def create_layout(app: Dash) -> html.Div:
    """Create the layout for the Dash app."""
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.tittle),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    nation_dropdown.render(app),
                ]
            ),
            bar_chart.render(app),
        ]
    )