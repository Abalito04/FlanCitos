# 🍮 FlanCitos — Sales Management System

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)](https://railway.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

> **EN:** A web-based sales and management system built for a small local business (FlanCitos). Handles daily sales tracking, product management, and basic reporting through a clean Flask interface.
>
> **ES:** Sistema web de ventas y gestión desarrollado para un pequeño negocio local (FlanCitos). Permite registrar ventas diarias, administrar productos y generar reportes básicos desde una interfaz simple en Flask.

---

## ✨ Features · Características

- 📊 **Daily sales tracking** — register and view sales by date
- 🧣 **Product management** — add, edit and remove products with prices
- 📅 **Sales history** — view past transactions and totals
- 📈 **Basic reporting** — daily revenue summary
- 🔐 **Simple admin interface** — protected management views
- 📱 **Responsive UI** — works on mobile and desktop

---

## 🗂️ Project Structure

```
FlanCitos/
├── app.py              # Flask application — routes and logic
├── templates/          # HTML templates (Jinja2)
├── requirements.txt    # Python dependencies
├── Procfile            # Railway deployment config
└── README.md
```

---

## 🚀 Quick Start · Instalación local

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/Abalito04/FlanCitos.git
cd FlanCitos

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

App will be available at `http://localhost:5000`

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python · Flask 3.1 |
| Templating | Jinja2 |
| Frontend | HTML5 · CSS3 |
| Server | Gunicorn |
| Deployment | Railway |

---

## 💡 What I Learned · Qué aprendí

This project was built to solve a **real problem for a real client** — a small local business that needed a simple digital tool to replace their paper-based sales tracking.

- Structuring a **Flask app from scratch** with clean route organization
- Working with **Jinja2 templates** for dynamic HTML rendering
- **Deploying a Flask app on Railway** with Gunicorn and Procfile
- Handling **real-world requirements** from a non-technical client

---

## 👨‍💻 Author

**Matias Abalo** — [@Abalito04](https://github.com/Abalito04)

🌐 [Portfolio](https://abalito.dev/) · ✉️ [abalito95@gmail.com](mailto:abalito95@gmail.com)
