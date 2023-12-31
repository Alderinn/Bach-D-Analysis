from appPlotly import createBubbles
from scanForString import searchData
from fix import fixMyBrokenCSV
import os

def main():
    # 1.a) Scan for string across all data
    searchData()
    print("Search Completed")
    # 1.b) fix csv output
    print("Starting fix CSV")
    fixMyBrokenCSV()
    # 2.) Use results.csv to open a plotly bubble graph
    createBubbles()
    os.remove("results.csv")
    os.remove("results(fixed).csv")
main()