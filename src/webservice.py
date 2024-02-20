#!/bin/python

from flask import Flask, request
import controller

app = Flask(__name__)

# Metodos de API REST
@app.route('/')
def saludo():
    return '¡Hola desde mi servicio!'

@app.route('/saludo/<persona>')
def saludoDinamico(persona):
    return 'Hola %s, bienvenido!!!' % persona

@app.route('/cuadrado/<float:num>')
def calculaCuadrado(num):
    resp = num * num
    return 'Respuesta: %f' %resp

@app.route('/test', methods=['POST', 'GET'])
def recibeParam():
    textReturn = "Método no aceptado"
    if request.method == "POST":
        data = request.get_json()
        try:
            mascota = data['mascota']
            numero = data['num'] * 2
            textReturn = 'Se recibio: %s,' % mascota
            textReturn = textReturn + ' por 2: %i' % numero
        except:
            textReturn = "Ocurrió un error"
    return textReturn 

@app.route('/rlineal', methods=['POST', 'GET'])
def preRLineal():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        vx = data['vx']
        vy = data['vy']
        x = data['x']
        return controller.getRLineal(vx, vy, x)

@app.route('/convertir', methods=['POST'])
def conversion():
    data = request.json
    if ('numero' not in data or 
            'base_actual' not in data or 
            'base_deseada' not in data):
        return json.dumps({"error": "Se requieren los campos 'numero', 'base_actual' y 'base_deseada'."}), 400
    numero = data['numero']
    base_actual = data['base_actual']
    base_deseada = data['base_deseada']
    return controller.convertir_base(numero, 
            base_actual, 
            base_deseada)

# Lanzamiento de Servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

