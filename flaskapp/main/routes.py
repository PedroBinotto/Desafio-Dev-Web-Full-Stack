from flask import render_template, request, Blueprint, flash, url_for, redirect, jsonify
from flaskapp import db
from flaskapp.models import Record
from flaskapp.main.forms import InputForm
from flaskapp.main.utils import calculate

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/home/<int:num1>/<int:num2>', methods=['GET', 'POST'])
def home(num1=None, num2=None):
	form = InputForm()
	if form.validate_on_submit():
		record = Record(num1=form.num1.data, num2=form.num2.data)
		db.session.add(record)
		db.session.commit()
		return redirect(url_for('main.home', num1=form.num1.data, num2=form.num2.data))
	if num1 and num2:
		lim_inf = min([num1, num2])
		lim_sup = max([num1, num2])
		results = calculate(lim_inf, lim_sup)

		return render_template('home.html', form=form, results=results)

	return render_template('home.html', form=form)

@main.route('/history')
def history():
	return render_template('history.html')

