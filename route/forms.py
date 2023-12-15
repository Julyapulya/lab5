from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddRegion(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class Delete(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    submit = SubmitField('Удалить')


class AddTaxParam(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    city_id = IntegerField('city_id', validators=[DataRequired()])
    from_hp_car = IntegerField('from_hp_car', validators=[DataRequired()])
    to_hp_car = IntegerField('to_hp_car', validators=[DataRequired()])
    from_production_year_car = IntegerField('from_production_year_car', validators=[DataRequired()])
    to_production_year_car = IntegerField('to_production_year_car', validators=[DataRequired()])
    rate = IntegerField('rate', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class Calc(FlaskForm):
    hp_base = IntegerField('hp_base', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])
    id = IntegerField('id', validators=[DataRequired()])
    submit = SubmitField('Считать')