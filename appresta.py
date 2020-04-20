
from flask import Flask, jsonify
from flask import request, Response

app = Flask(__name__)
@app.route('/resta', methods=["get"])
def resta():
    if request.method=="GET" and len(request.args)>0:
        num1=request.args.get("num1")
        num2=request.args.get("num2")
        operador = '-'
        try:
            resultado = eval(num1 + operador + num2)
        except:
            return jsonify({"Resultado1":' Los datos no se pueden restar' })

        return jsonify({'Numero 1': num1, 'Numero 2': num2, 'Resultado =': resultado,})
    else:
        return jsonify({"Resultado1": "No hay parametros en el GET"  })
		
if __name__ == '__main__':
    app.run(debug=True, port=9000)