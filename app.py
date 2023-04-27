import pandas as pd
from dash import Dash, dcc, html

data = (
pd.read_csv("avocado.csv")
    .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)