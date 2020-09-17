from flask import render_template, url_for, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from project.quick_check.forms import Form
from project import db
from project.models import Block1

check_blueprint = Blueprint('quick_check', __name__, template_folder='templates')

# testfrage1
@check_blueprint.route('/check', methods=['GET', 'POST'])
@login_required
def quick_check():
    form = Form()
    print(form.errors)
    user_id = current_user.id
    output = Block1.query.first()
    spider_value1 = 0
    spider_value2 = 0
    spider_value3 = 0
    spider_value4 = 0
    spider_value5 = 0
    spider_value6 = 0
    if form.validate_on_submit():
        ergebnis = []
        for items in Block1.query.all():
            delete_item = Block1.query.get(items.report_frage1_id())
            db.session.delete(delete_item)
            db.session.commit()
        frage1 = form.frage1.data
        if frage1 < 3:
            ergebnis.append("Ihre Strategischen Ziele passen nicht zum Subscription Geschäftsmodell.")
        frage2 = form.frage2.data
        if frage2 < 3:
            ergebnis.append("Es gibt Optimierungspotenzial beim Leistungssystem.")
        frage3 = form.frage3.data
        if frage3 < 3:
            ergebnis.append("Die IT-Infrastruktur ist verbesserungswürdig.")
        frage4 = form.frage4.data
        if frage4 < 3:
            ergebnis.append("Die Serviceorganisation kann noch nicht ganz mithalten.")
        frage5 = form.frage5.data
        if frage5 < 3:
            ergebnis.append("Sie sollten einen eigenen Vertriebskanal etablieren.")
        frage6 = form.frage6.data
        if frage6 < 3:
            ergebnis.append("Prüfen Sie externe Finanzierungslösungen...")
        len_ergebnis = len(ergebnis)
        if len_ergebnis < 1:
            ergebnis.append("Herzlichen Glückwunsch. Sie sind Subscription Ready!")
        else:
            ergebnis.append("Schauen Sie sich zu diesen Themen im Canvas um oder Kontaktieren Sie unser Projektteam!")
        db_wert = Block1(user_id, frage1, frage2, frage3, frage4, frage5, frage6)
        db.session.add(db_wert)
        db.session.commit()
        sum_fragen = frage1+frage2+frage3+frage4+frage5+frage6
        spider_value1 = frage1
        spider_value2 = frage2
        spider_value3 = frage3
        spider_value4 = frage4
        spider_value5 = frage5
        spider_value6 = frage6
        output = Block1.query.first()
        return render_template('quick_check.html', form=form, len_ergebnis=len_ergebnis,ergebnis=ergebnis, output=output, spider_value1=spider_value1, spider_value2=spider_value2, spider_value3=spider_value3, spider_value4=spider_value4, spider_value5=spider_value5, spider_value6=spider_value6)
    return render_template('quick_check.html', form=form, output=output, spider_value1=spider_value1, spider_value2=spider_value2, spider_value3=spider_value3, spider_value4=spider_value4, spider_value5=spider_value5, spider_value6=spider_value6)