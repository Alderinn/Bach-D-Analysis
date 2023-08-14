from dash import Dash
from dash import dcc
from dash import html
import pandas as pd
filename = "S08Emta.csv"
filename = "07x07_-_Week_7_(Season_7).txt.csv"

data = pd.read_csv("csv/"+filename)
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Bachelor Analylitics",),
        html.P(
            children="Let's look at some data from the show"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["phrase"],
                        "y": data['freq'],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Most Common Phrases"},
            },
        ),
    ]
)
if __name__ == "__main__":
    app.run_server(debug=True)