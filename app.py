import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input,Output

data = (
pd.read_csv("avocado.csv")
    # .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

regions = data["region"].sort_values().unique()
avocado_types = data["type"].sort_values().unique()

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id="type-filter",
                    options=[
                        {"label": avocado_type.title(), "value": avocado_type}
                        for avocado_type in avocado_types
                    ],
                    value="conventional",
                    clearable=False,
                    # className="dropdown",
                ),
                dcc.Dropdown(
                    id="region-filter",
                    options=[
                        {"label": region, "value": region}
                        for region in regions
                    ],
                    value="Albany",
                    clearable=False,
                    # className="dropdown",
                )
            ]
        ),
        dcc.Graph(
            id="price-chart",
            config={"displayModeBar": False}
        )
    ]
)

@app.callback(
    Output("price-chart", "figure"),
    Input("type-filter", "value"),
    Input("region-filter", "value"),
)
def update_charts(avocado_type, region):
    filtered_data = data.query(
        "type == @avocado_type and region == @region"
    )

    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
            },
        ],
        "layout": {"title": "Average Price of Avocados"},
    }

    return price_chart_figure

if __name__ == "__main__":
    app.run_server(debug=True)