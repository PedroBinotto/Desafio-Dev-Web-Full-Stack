from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class InputForm(FlaskForm):
	num1 = IntegerField('Inserir Valor do Número...', validators=[DataRequired()])
	num2 = IntegerField('Inserir Valor do Número...', validators=[DataRequired()])

	submit =  SubmitField('Calcular Números')
