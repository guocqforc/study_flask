#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired

class NameForm(Form):
    name = StringField('what is you name?', validators=[Required()])
    submit = SubmitField('Submit', validators=[])