from flask import Flask, render_template, request, redirect, url_for, send_file
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
            # enumerate nos da el número de línea (i) automáticamente
            for i, linea in enumerate(archivo):
                if linea.strip():
                    partes = linea.strip().split('|')
                    if len(partes) == 4:
                        ventas.append({
                            'id_real': i,  # <--- GUARDAMOS LA POSICIÓN REAL
                            'fecha': partes[0],
                            'turno': partes[1],
                            'cliente': partes[2],
                            'cantidad': int(partes[3])
                        })
    # OJO: Sacá el [::-1] (reverso) si lo tenías, porque nos complica borrar por ahora.
    return ventas # Devolvemos en orden de carga


def guardar_venta(cliente, cantidad, turno):
    # Obtenemos la fecha de hoy (ej: 19/12/2025)
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")
    
    with open(ARCHIVO_VENTAS, 'a', encoding='utf-8') as archivo:
        # Guardamos: Fecha|Turno|Cliente|Cantidad
        archivo.write(f"{fecha_hoy}|{turno}|{cliente}|{cantidad}\n")

@app.route('/')
def inicio():
    # 1. Cargamos TODO el historial
    todas_las_ventas = cargar_ventas()    
    # 2. Obtenemos la fecha de hoy
    fecha_hoy = datetime.now().strftime("%d/%m/%Y")    
    # 3. FILTRADO: Solo las de hoy
    ventas_hoy = [v for v in todas_las_ventas if v['fecha'] == fecha_hoy]    
    # 4. Total de hoy
    total_hoy = sum([v['cantidad'] for v in ventas_hoy])
    
    return render_template('index.html', ventas=ventas_hoy, total=total_hoy)

@app.route('/agregar', methods=['POST'])
def agregar_venta():
    cliente = request.form['cliente']
    cantidad = int(request.form['cantidad'])
    turno = request.form['turno'] # <--- Recibimos el turno
    
    guardar_venta(cliente, cantidad, turno)
    
    return redirect(url_for('inicio'))

@app.route('/descargar')
def descargar_historial():
    # send_file hace todo el trabajo sucio: busca el archivo y te lo manda al navegador
    # as_attachment=True fuerza la descarga en vez de mostrarlo en pantalla
    return send_file(ARCHIVO_VENTAS, as_attachment=True, download_name="historial_ventas.txt")

@app.route('/eliminar/<int:indice>')
def eliminar_venta(indice):
    # 1. Cargamos todas las ventas (pero necesitamos las líneas crudas para reescribir)
    if os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        # 2. Verificamos que el índice sea válido (que exista esa línea)
        if 0 <= indice < len(lineas):
            # 3. La borramos de la lista en memoria
            del lineas[indice]
            
            # 4. Sobrescribimos el archivo con la lista nueva (sin la borrada)
            with open(ARCHIVO_VENTAS, 'w', encoding='utf-8') as archivo:
                archivo.writelines(lineas)
    
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
