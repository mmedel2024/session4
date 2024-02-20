#!/bin/python3
import json

def getRLineal(v_x, v_y, x_pos):
    n = len(v_x)
    x, y, xy, xx = [0.0 for _ in range(4)]
    for i in range(n):
        x += v_x[i]
        y += v_y[i]
        xy += v_x[i] * v_y[i]
        xx += v_x[i] ** 2
    m = ((n * xy) - (x * y)) / ((n * xx) - (x **2))
    b = (y - (m * x)) / n
    y_obj = (m * x_pos) + b
    return json.dumps({"status": "ok", "y_obj": y_obj})

def convertir_base(numero, base_actual, base_deseada):
    try:
        # Convertir el número de la base actual a decimal
        decimal_numero = int(str(numero), base_actual)
        # Convertir el número decimal a la base deseada
        resultado = format(decimal_numero, f'0{base_deseada}x') if base_deseada == 16 else format(decimal_numero, f'0{base_deseada}b')
        return json.dumps({"status": "ok", "resultado": resultado})
    except ValueError:
        return json.dumps({"Error": "El número proporcionado no es válido."})

