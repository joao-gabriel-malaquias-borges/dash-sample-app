from dash import dcc
from data.dataset import dataFrame

avocado_types = dataFrame['type'].sort_values().unique()

type_filter = dcc.Dropdown(
    id="type-filter",
    options=[
        { "label": avocado_type.title(), "value": avocado_type }
        for avocado_type in avocado_types
    ],
    value="conventional",
    clearable=False,
    # className="dropdown",
)