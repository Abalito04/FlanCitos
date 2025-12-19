from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Si estamos en Railway (o Linux), usamos una ruta absoluta. 
# Si estamos en Windows (tu PC), usamos el archivo local.
if os.name == 'nt':  # Windows
    RUTA_BASE = os.getcwd()
else:                # Linux (Railway)
    RUTA_BASE = '/app/data' 

if not os.path.exists(RUTA_BASE) and os.name != 'nt':
    os.makedirs(RUTA_BASE)

# Nombre del archivo donde guardamos las ventas
ARCHIVO_VENTAS = os.path.join(RUTA_BASE, 'ventas.txt')



# Función para cargar las ventas desde el archivo
def cargar_ventas():
    ventas = []
    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                if linea.strip():  # Si la línea no está vacía
                    partes = linea.strip().split('|')
                    if len(partes) == 2:
                        cliente = partes[0]
                        cantidad = int(partes[1])
                        ventas.append({'cliente': cliente, 'cantidad': cantidad})
    return ventas

# Función para guardar una venta en el archivo
def guardar_venta(cliente, cantidad):
    with open(ARCHIVO_VENTAS, 'a', encoding='utf-8') as archivo:
        archivo.write(f"{cliente}|{cantidad}\n")

@app.route('/')
def inicio():
    ventas = cargar_ventas()
    total = sum([v['cantidad'] for v in ventas])
    ventas_texto = [f"{v['cliente']} - {v['cantidad']} flan(es)" for v in ventas]
    return render_template('index.html', ventas=ventas_texto, total=total)

@app.route('/agregar', methods=['POST'])
def agregar_venta():
    cliente = request.form['cliente']
    cantidad = int(request.form['cantidad'])
    
    # Guardamos la venta en el archivo
    guardar_venta(cliente, cantidad)
    
    # Redirigimos a la página principal
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
