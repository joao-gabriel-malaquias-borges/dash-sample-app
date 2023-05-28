import pandas as pd

dataFrame = (
    pd.read_csv("./data/avocado.csv")
        # .query("type == 'conventional' and region == 'Albany'")
        .assign(Date = lambda dataFrame: pd.to_datetime(dataFrame['Date'], format="%Y-%m-%d"))
        .sort_values(by = 'Date')
)