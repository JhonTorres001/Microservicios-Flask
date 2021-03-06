from flask_wtf import FlaskForm
from wtforms import Form, IntegerField,SelectField,SubmitField
from wtforms.validators import Required	


class formsumar(FlaskForm):                      
	num1=IntegerField("Número1",validators=[Required("Tienes que introducir el dato")])
	num2=IntegerField("Número2",validators=[Required("Tienes que introducir el dato")])
	operador=SelectField("Operador",choices=[("+","Sumar")])
	submit = SubmitField('Submit')