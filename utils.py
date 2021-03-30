import pymysql
import pandas as pd
from sql_queries import list_top_n_movies_by_gross_revenue, billion_dollar_movies, \
    list_of_movies_with_biggest_losses, highest_rated_movies, actor_know_for
from credentials import pwd
import numpy as np


def conn():
    mydb = pymysql.connect(host='localhost',
                           user='root',
                           password=pwd,
                           database="Movies",
                           cursorclass=pymysql.cursors.DictCursor)
    return mydb.cursor()


def db_exe(query, c):
    try:
        if c.connection:
            c.execute(query)
            return c.fetchall()
        else:
            c = conn()
    except Exception as e:
        return str(e)


num_format = lambda x: '{:,}'.format(x)


def build_formatters(df, format):
    return {column: format for (column, dtype) in df.dtypes.iteritems() if
            dtype in [np.dtype('int64'), np.dtype('float64')]}


def handle_query(sql_query):
    dbc = conn()
    data = None
    # print(sql_query)
    try:
        results = db_exe(sql_query, dbc)

        # print(type(results))
    except TypeError as e:
        results = e
    if isinstance(results, list):
        results = pd.DataFrame.from_dict(results)
        print(results.dtypes)
        # TODO: Add graphing function here

        data = {
            "query": sql_query,
            "results": results.to_html(index=False,
                                       formatters=build_formatters(results, num_format),
                                       classes="table table-striped table-borderless align-middle"),
            "graph": None
        }
    elif isinstance(results, str):
        data = {
            "query": sql_query,
            "results": f"Error in query: {results}"
        }
    else:
        data = {
            "query": sql_query,
            "results": f"""
            <div class="alert alert-primary" role="alert">
                Looks like there are no results with this query. Please try another.
            </div>
            """
        }

    return data


def handle_custom_form(form):
    sql_query = f"{form.sqlQuery.data}"
    return sql_query


def handle_minimum_user_input_form(form):
    sql_type = form.query_type.data
    sql_sort = form.sorting.data
    sql_limit = form.limit.data
    sql_string_value = form.string_value.data
    # print(sql_type, sql_sort,sql_limit, sql_string_value)
    return sql_sort, sql_limit, sql_type, sql_string_value


def list_of_customizable_queries(user_input, sql_sort, sql_limit, name):
    if user_input == "by gross revenue":
        return list_top_n_movies_by_gross_revenue(sql_sort, sql_limit)
    if user_input == "with billion dollars gross revenue":
        return billion_dollar_movies(sql_sort, sql_limit)
    if user_input == "by profit loss":
        return list_of_movies_with_biggest_losses(sql_sort, sql_limit)
    if user_input == "by user rating":
        return highest_rated_movies(sql_sort, sql_limit)
    if user_input == "is known for":
        return actor_know_for(name, sql_sort, sql_limit)


def query_string(sql_sort, sql_limit, sql_type, sql_string_value):
    if sql_sort == "DESC":
        sql_sort = "top"
    elif sql_sort == "ASC":
        sql_sort = "bottom"
    if len(sql_string_value) > 0:
        sql_type = "is known for order by year"
    string = f"Choose {sql_sort} {sql_limit} movies {sql_string_value} {sql_type}"
    return string

# submit too big
# aligh closer together
# Choose and movies bigger
