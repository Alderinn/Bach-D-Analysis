from appPlotly import createBubbles
from scanForString import searchData
def main():
    # 1.a) Scan for string across all data
    searchData()
    # 1.b) fix csv output
    



    # 2.) Use results.csv to open a plotly bubble graph
    createBubbles()


main()