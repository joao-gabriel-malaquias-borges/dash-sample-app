from dash import Dash, dcc, html
from src.components.type_filter import type_filter
from src.components import price_chart
from data.dataset import dataFrame

regions = dataFrame['region'].sort_values().unique()
avocado_types = dataFrame['type'].sort_values().unique()

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                type_filter,
                dcc.Dropdown(
                    id="region-filter",
                    options=[
                        { "label": region, "value": region }
                        for region in regions
                    ],
                    value="Albany",
                    clearable=False,
                    # className="dropdown",
                )
            ]
        ),
        price_chart.render(app)
    ]
)

if __name__ == '__main__':
    app.run_server(debug = True)