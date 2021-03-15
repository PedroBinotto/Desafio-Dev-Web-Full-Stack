from flask import render_template, request, Blueprint, flash, url_for, redirect
from flaskapp import db
from flaskapp.models import Record
from flaskapp.main.forms import InputForm
from flaskapp.main.utils import calculate

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/home/<string:num1>/<string:num2>', methods=['GET', 'POST'])
def home(num1=None, num2=None):
	title = 'Calcular'
	form = InputForm()
	if form.validate_on_submit():
		record = Record(num1=form.num1.data, num2=form.num2.data)
		db.session.add(record)
		db.session.commit()
		return redirect(url_for('main.home',
			title=title,
			num1=str(form.num1.data) if form.num1.data >= 0 else '0',
			num2=str(form.num2.data) if form.num2.data >= 0 else '0'
		))
	if num1 and num2:
		lim_inf = int(min([num1, num2]))
		lim_sup = int(max([num1, num2]))
		results = calculate(lim_inf, lim_sup)
		return render_template('home.html',
			title=title,
			form=form,
			results=results,
			lim_inf=lim_inf,
			lim_sup=lim_sup
		)
	return render_template('home.html', title=title,form=form)

@main.route('/history')
def history():
	page = request.args.get('page', 1, type=int)
	records = Record.query.order_by(Record.date_added.desc()).paginate(page=page, per_page=50)
	next_url = url_for('main.history', page=records.next_num)\
		if records.has_next else None
	prev_url = url_for('main.history', page=records.prev_num)\
		if records.has_prev else None
	return render_template("history.html",
		title='Histórico',
		records=records.items,
		next_url=next_url,
		prev_url=prev_url
	)

