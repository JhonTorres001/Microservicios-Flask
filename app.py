from flask import Flask
from flask import request, Response, send_from_directory, render_template, request
from forms import formcalculadora

app = Flask(__name__)

app.secret_key = 'clave de cifrado lo más robusta posible'
@app.route("/calculadora_post", methods=["get","post"])
def calculadora_post():
	form=formcalculadora(request.form)
	if form.validate_on_submit():
		num1=form.num1.data
		num2=form.num2.data
		operador=form.operador.data
		try:
			resultado=eval(str(num1)+operador+str(num2))
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
	else:
		
		return render_template("calculadora_post.html",form=form)	


if __name__ == '__main__':
    app.run(debug=True, port=4000)