from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, ValidationError

class InputForm(FlaskForm):
	num1 = IntegerField(validators=[InputRequired('Você precisa informar um número!')], render_kw={'placeholder': 'Inserir Valor do Número (1)'})
	num2 = IntegerField(validators=[InputRequired('Você precisa informar um número!')], render_kw={'placeholder': 'Inserir Valor do Número (2)'})

	submit =  SubmitField('Calcular Números')
