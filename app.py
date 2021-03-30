from flask import Flask, render_template, request
from forms import WriteYourOwnQuery, MinimumUserInput
from utils import handle_custom_form, handle_minimum_user_input_form, handle_query, list_of_customizable_queries, query_string
import altair as alt
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = 'development_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    form_write_your_own_query = WriteYourOwnQuery()
    form_customizable = MinimumUserInput()
    print("back to index")

    return render_template("index.html", form_write_your_own_query=form_write_your_own_query,
                           form_customizable=form_customizable)


@app.route('/writeyourownquery', methods=['GET', 'POST'])
def write_your_own_query():
    form_write_your_own_query = WriteYourOwnQuery()
    form_customizable = MinimumUserInput()
    if request.method == "POST":
        if form_write_your_own_query.validate_on_submit():
            sql_query = handle_custom_form(form_write_your_own_query)
            data = handle_query(sql_query)
            return render_template("index.html", data=data, form_write_your_own_query=form_write_your_own_query,
                                   form_customizable=form_customizable)


@app.route('/customizable', methods=['GET', 'POST'])
def customizable():
    form_write_your_own_query = WriteYourOwnQuery()
    form_customizable = MinimumUserInput()
    if request.method == "POST" and form_customizable.validate_on_submit():
        sql_sort, sql_limit, sql_type, sql_string_value = handle_minimum_user_input_form(form_customizable)
        sql_query = list_of_customizable_queries(sql_type, sql_sort, sql_limit, sql_string_value)
        data = handle_query(sql_query)
        string_q = query_string(sql_sort, sql_limit, sql_type, sql_string_value)

        df = pd.DataFrame({
            "x": ['A', 'B', 'C', 'D', 'E'],
            "y": [5, 6, 7, 8, 9]})
        chart = alt.Chart(df).mark_bar().encode(
            x='x',
            y='y',
        )
        chart_json = chart.to_dict()
        #print(chart_json)
        return render_template("index.html", data=data, form_write_your_own_query=form_write_your_own_query,
                               form_customizable=form_customizable, string_q=string_q, chart=chart_json)


if __name__ == '__main__':
    app.run(debug=True)
