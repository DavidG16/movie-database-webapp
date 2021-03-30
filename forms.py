from wtforms import SubmitField, SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class WriteYourOwnQuery(FlaskForm):
    sqlQuery = TextAreaField(label="Write SQL Query",
                             validators=[InputRequired()])
    submit = SubmitField(label='Search', id="submit-q-1")
    submit = SubmitField(label='Search', id="submit-q-1")


class MinimumUserInput(FlaskForm):
    """
    Form with minimum user input.
    Input is limited to query name, sorting and limit.
    """
    query_type = SelectField(label="Query Type", choices=["by gross revenue",
                                                          "with billion dollars gross revenue",
                                                          "by profit loss",
                                                          "by user rating",
                                                          "is known for"],
                             validators=[InputRequired(message="Error")], id="queryType")
    limit = StringField(label="Limit", default=10,
                        validators=[InputRequired(message="Error")], id="limit")
    sorting = SelectField(label='Choose', choices=[('ASC', 'bottom'), ('DESC', "top")],
                          validators=[InputRequired(message="Error")], default="DESC", id="sorting")

    string_value = StringField(label="movies", id="string-val")
    submit = SubmitField(label="Search", id="submit-q-2")
