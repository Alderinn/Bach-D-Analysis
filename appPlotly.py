import pandas as pd
import plotly.express as px


def createBubbles():
    # Load data from CSV file
    data = pd.read_csv("results(fixed).csv")
    # Create a bubble chart
    fig = px.scatter(data, x="episode", y="season",
                    size="count", color="count",
                    hover_name="count", log_x=True, size_max=60,
                    title="Bubble Chart of Episode Counts by Season")
    fig.update_layout(
        xaxis_title="Episode",
        yaxis_title="Season",
        legend_title="Season"
    )
    fig.show()