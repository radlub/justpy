import justpy as jp
import pandas
import os
from datetime import datetime
from pytz import utc
data = pandas.read_csv("reviews.csv", parse_dates = ["Timestamp"])

data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby(["Day"]).mean()


def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h2 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="There graphs represents course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = ("Average Rating by Day")

    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average["Rating"])


    return wp


jp.justpy(app)