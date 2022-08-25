from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


class ActorInnerJoinForm(FlaskForm):
    actor1 = StringField('First Actor', validators=[DataRequired(), Length(min=2)])
    actor2 = StringField('Second Actor', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('InnerJoin!')
