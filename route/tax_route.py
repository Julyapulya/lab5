from flask import Blueprint, render_template
from config import db

from route.forms import Calc
from route.object import CarTaxParam

tax_route = Blueprint('tax_route', __name__)


@tax_route.route('/v1/car/tax/calc', methods=['GET', 'POST'])
def calculation():
    tax = None
    form = Calc()
    if form.validate_on_submit():
        hp_base = int(form.hp_base.data)
        year = int(form.year.data)
        code = int(form.id.data)

        object_rate = db.session.query(CarTaxParam.rate).filter(CarTaxParam.from_hp_car < hp_base,
                                                                hp_base < CarTaxParam.to_hp_car,
                                                                CarTaxParam.from_production_year_car < year,
                                                                year < CarTaxParam.to_production_year_car,
                                                                CarTaxParam.id == code).first()
        rate = float(object_rate[0])
        tax = rate * hp_base
        context = {
            'tax': tax,
            'message': 'Успешно',
            'status': 200
        }
    else:
        context = {
            'message': 'Ошибка',
            'status': 400
        }
    return render_template('index.html', **context, form=form)