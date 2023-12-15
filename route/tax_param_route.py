from flask import Blueprint, render_template

from route.forms import AddTaxParam, Delete
from route.object import Region, CarTaxParam
from config import db

tax = Blueprint('tax', __name__)


@tax.route('/v1/car/tax-param/add', methods=['POST', 'GET'])
def add():
    form = AddTaxParam()
    if form.validate_on_submit():
        code = form.id.data
        city_id = form.city_id.data
        from_hp_car = form.from_hp_car.data
        to_hp_car = form.to_hp_car.data
        from_production_year_car = form.from_production_year_car.data
        to_production_year_car = form.to_production_year_car.data
        rate = form.rate.data
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            context = {
                'message': 'Регион пуст',
                'status': 200
            }
            return render_template('tax-param-add.html', **context, form=form)

        object_rate = CarTaxParam.query.filter_by(from_hp_car=from_hp_car, to_hp_car=to_hp_car,
                                                  from_production_year_car=from_production_year_car,
                                                  to_production_year_car=to_production_year_car, id=code).all()
        if object_rate:
            context = {
                'message': 'Заполнено',
                'status': 200
            }
            # message = {'message': 'Заполнено'}
            return render_template('tax-param-add.html', **context, form=form)

        newCar_tax_param = CarTaxParam(id=code,
                                       city_id=city_id,
                                       from_hp_car=from_hp_car,
                                       to_hp_car=to_hp_car,
                                       from_production_year_car=from_production_year_car,
                                       to_production_year_car=to_production_year_car,
                                       rate=rate
                                       )
        db.session.add(newCar_tax_param)
        db.session.commit()
        context = {
            'message': 'Успешно',
            'status': 200
        }
    else:
        context = {
            'message': 'Ошибка',
            'status': 200
        }

    return render_template('tax-param-add.html', **context, form=form)


@tax.route('/v1/car/tax-param/update', methods=['POST', 'GET'])
def update():
    form = AddTaxParam()
    if form.validate_on_submit():
        code = form.id.data
        city_id = form.city_id.data
        from_hp_car = form.from_hp_car.data
        to_hp_car = form.to_hp_car.data
        from_production_year_car = form.from_production_year_car.data
        to_production_year_car = form.to_production_year_car.data
        rate = form.rate.data
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            context = {
                'message': 'Успешно',
                'status': 200
            }
            return render_template('tax-param-update.html', **context)
        object_rate = CarTaxParam.query.filter(CarTaxParam.id == code).all()
        if object_rate is None:
            context = {
                'message': 'Заполнено',
                'status': 200
            }
            return render_template('tax-param-update.html', **context)
        city = CarTaxParam.query.filter(CarTaxParam.id == code).first()
        if city:
            city.id = code
            city.city_id = city_id
            city.from_hp_car = from_hp_car
            city.to_hp_car = to_hp_car
            city.from_production_year_car = from_production_year_car
            city.to_production_year_car = to_production_year_car
            city.rate = rate
            db.session.commit()
            context = {
                'message': 'Успешно',
                'status': 200
            }
            return render_template('tax-param-update.html', **context, form=form)
    else:
        context = {
            'message': 'Введите данные',
            'status': 200
        }
        return render_template('tax-param-update.html', **context)


@tax.route('/v1/car/tax-param/delete', methods=['POST', 'GET'])
def delete():
    form = Delete()
    if form.validate_on_submit():
        code = int(form.id.data)
        code_base = Region.query.filter(CarTaxParam.id == code).all()
        if code_base is None:
            context = {
                'message': 'Ошибка',
                'status': 400
            }
            return render_template('tax-param-delete.html', **context)
        CarTaxParam.query.filter(CarTaxParam.id == code).delete()
        db.session.commit()
        context = {
            'message': 'Успешно',
            'status': 200
        }
    else:
        context = {
            'message': 'Введите данные',
            'status': 200
        }
    return render_template('tax-param-delete.html', **context, form=form)


@tax.route('/v1/car/tax-param/get/all', methods=['GET'])
def fetch():
    code_base = db.session.query(CarTaxParam.id, CarTaxParam.city_id, CarTaxParam.from_hp_car,
                                 CarTaxParam.to_hp_car, CarTaxParam.from_production_year_car,
                                 CarTaxParam.to_production_year_car, CarTaxParam.rate).all()
    return render_template('tax-param-list.html', code_base=code_base)
