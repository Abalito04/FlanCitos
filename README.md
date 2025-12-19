# 🍮 FlanCitos - Control de Ventas

**FlanCitos** es una aplicación web minimalista y responsive diseñada para gestionar las ventas diarias de un emprendimiento de postres caseros. Permite registrar pedidos, calcular totales del día y exportar el historial completo.

---

## 🚀 Características

- **Registro Rápido:** Formulario simple para cargar cliente, cantidad y turno (Mañana/Noche).
- **Caja Diaria Automática:** Filtra y muestra solo las ventas de la fecha actual con su total acumulado.
- **Historial Seguro:** Almacenamiento persistente en archivo de texto (`ventas.txt`).
- **Gestión de Errores:** Posibilidad de eliminar ventas cargadas incorrectamente.
- **Exportación:** Botón para descargar el historial completo de ventas.
- **Diseño Responsive:** Interfaz optimizada para uso cómodo desde celulares.

---

## 🛠️ Tecnologías Usadas

- **Python 3.x**
- **Flask** (Framework web)
- **HTML5 / CSS3** (Diseño y estructura)
- **Gunicorn** (Servidor de producción)

---

## 💻 Instalación y Uso Local

1. **Clonar el repositorio:**

git clone https://github.com/Abalito04/FlanCitos
cd FlanCitos

2. **Crear un entorno virtual (recomendado):**

python -m venv venv
source venv/bin/activate # En Linux/Mac
venv\Scripts\activate # En Windows

3. **Instalar dependencias:**

pip install -r requirements.txt

4. **Ejecutar la aplicación:**

python app.py

5. **Abrir en el navegador:**

Ingresa a `http://localhost:5000`

---

## ☁️ Despliegue en Railway

Este proyecto está configurado para desplegarse fácilmente en **Railway**:

1. Conectar el repositorio de GitHub a Railway.
2. Configurar un **Volumen** persistente en la ruta `/app/data` para evitar perder datos al reiniciar.
3. Railway detectará automáticamente el archivo `Procfile` y `requirements.txt`.

---

## 📝 Estructura del Archivo de Datos

Las ventas se guardan en `ventas.txt` con el siguiente formato (pipe-separated):
Ejemplo: `19/12/2025|Mañana|Juan|2` - DD/MM/AAAA|Turno|Cliente|Cantidad

---

**Desarrollado por Matias Abalo para el control del imperio del flan.**

