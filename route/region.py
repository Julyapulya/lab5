from flask import Blueprint, render_template
from route.forms import AddRegion, Delete
from route.object import Region

from config import db

region = Blueprint('region', __name__)


@region.route('/v1/region/add', methods=['POST', 'GET'])
def taxes():
    form = AddRegion()
    if form.validate_on_submit():
        code = int(form.id.data)
        name = form.name.data

        code_base = db.session.query(Region.id).filter(Region.id == code).first()
        if code_base:
            context = {
                'message': 'Регион уже существует',
                'status': 400
            }
            # message = "Ошибка"
            return render_template('region-add.html', **context, form=form)
        newRegion = Region(id=code,
                           name=name)
        db.session.add(newRegion)
        db.session.commit()
        context = {
            'message': 'Регион успешно добавлен',
            'status': 200
        }
    else:
        context = {
            'message': 'Введите данные',
            'status': 200
        }

    return render_template('region-add.html', **context, form=form)


@region.route('/v1/region/update', methods=['POST', 'GET'])
def update():
    form = AddRegion()
    if form.validate_on_submit():
        code = int(form.id.data)
        name = form.name.data
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            context = {
                'message': 'Регион пуст',
                'status': 400
            }
            # message = 'Регион не заполнен'
            return render_template('region-update.html', **context, form=form)
        region_update = Region.query.filter(Region.id == code).first()
        if region_update:
            region_update.id = code
            region_update.name = name
            db.session.commit()
            context = {
                'message': 'Регион обновлён',
                'status': 400
            }
            return render_template('region-update.html', **context, form=form)
    else:
        context = {
            'message': 'Введите данные',
            'status': 200
        }
        return render_template('region-update.html', **context)


@region.route('/v1/region/delete', methods=['POST', 'GET'])
def delete():
    form = Delete()
    if form.validate_on_submit():
        code = int(form.id.data)
        print(code)
        code_base = db.session.query(Region.id, Region.name).filter(Region.id == code).all()
        if code_base is None:
            context = {
                'message': 'Ошибка',
                'status': 400
            }
            return render_template('region-delete.html', **context)
        city = Region.query.filter(Region.id == code).first()
        db.session.delete(city)
        db.session.commit()
        context = {
            'message': 'Успешно удален',
            'status': 200
        }
    else:
        context = {
            'message': 'Введите данные',
            'status': 400
        }
    return render_template('region-delete.html', **context)


@region.route('/v1/web/region', methods=['GET'])
def fetch():
    code_base = db.session.query(Region.name).all()
    return render_template('region-list.html', code_base=code_base)
