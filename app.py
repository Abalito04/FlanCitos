from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime # <--- Importante: agregá esto arriba

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



def cargar_ventas():
    ventas = []
    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                if linea.strip():
                    partes = linea.strip().split('|')
                    # Ahora esperamos 4 partes: Fecha|Turno|Cliente|Cantidad
                    if len(partes) == 4:
                        ventas.append({
                            'fecha': partes[0],
                            'turno': partes[1],
                            'cliente': partes[2],
                            'cantidad': int(partes[3])
                        })
    # Opcional: Invertir la lista para ver lo último primero
    return ventas[::-1] 

def guardar_venta(cliente, cantidad, turno):
    # Obtenemos la fecha de hoy (ej: 19/12/2025)
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
    
    with open(ARCHIVO_VENTAS, 'a', encoding='utf-8') as archivo:
        # Guardamos: Fecha|Turno|Cliente|Cantidad
        archivo.write(f"{fecha_hoy}|{turno}|{cliente}|{cantidad}\n")

@app.route('/')
def inicio():
    ventas = cargar_ventas()
    total = sum([v['cantidad'] for v in ventas])
    # Ya no armamos el texto acá, pasamos la lista de objetos completa al HTML
    return render_template('index.html', ventas=ventas, total=total)

@app.route('/agregar', methods=['POST'])
def agregar_venta():
    cliente = request.form['cliente']
    cantidad = int(request.form['cantidad'])
    turno = request.form['turno'] # <--- Recibimos el turno
    
    guardar_venta(cliente, cantidad, turno)
    
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
