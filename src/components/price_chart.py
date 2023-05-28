from dash import Dash, dcc, Input, Output
from data.dataset import dataFrame

def render(app: Dash) -> dcc.Graph:
    @app.callback(
        Output("price-chart", "figure"),
        Input("type-filter", "value"),
        Input("region-filter", "value"),
    )
    def update_chart(avocado_type, region):
        filtered_data = dataFrame.query(
            "type == @avocado_type and region == @region"
        )

        price_chart_figure = {
            "data": [
                {
                    "x": filtered_data["Date"],
                    "y": filtered_data["AveragePrice"],
                    "type": "lines",
                }
            ],
            "layout": { "title": "Average Price of Avocados" },
        }

        return price_chart_figure

    return dcc.Graph(
        id="price-chart",
        config={ "displayModeBar": False }
    )