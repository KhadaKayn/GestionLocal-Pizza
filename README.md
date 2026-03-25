# 🍕 GestiónLocal Pizza – Django Starter for Business Systems


![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Django](https://img.shields.io/badge/Framework-Django-092E20?logo=django)
![Status](https://img.shields.io/badge/Status-Base%20Template-blue)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
<img width="1917" height="867" alt="pizza2" src="https://github.com/user-attachments/assets/eb1df0f3-77e3-4c62-acd4-447af868dbf9" />


---

## ⚙️ Descripción
<img width="1917" height="875" alt="pizza" src="https://github.com/user-attachments/assets/afbb8291-53d9-4766-bfe8-4f1c3826c9d2" />

**GestiónLocal Pizza** es una base de sistema web desarrollada con Django orientada a la gestión de productos en un negocio tipo pizzería.

El proyecto está diseñado como una **plantilla escalable**, permitiendo administrar productos complejos (ingredientes, tamaños, masas, pizzas completas) y servir como punto de partida para sistemas más avanzados.

---

## 🎯 Objetivo del proyecto

👉 Proveer una base funcional para desarrollar sistemas de gestión de negocios.

El repositorio permite a otros desarrolladores comenzar desde una estructura ya implementada, enfocándose en extender funcionalidades en lugar de configurar el proyecto desde cero.

---

## 🚀 Funcionalidades
<img width="1917" height="868" alt="pizza3" src="https://github.com/user-attachments/assets/16d055fe-019a-4679-bfb0-cbacb9eaf28b" />

* 🍕 Gestión de productos (pizzas)
* 🧩 Configuración de elementos:

  * Ingredientes
  * Tamaños
  * Tipos de masa
* 👤 Registro de usuarios
* 🔐 Sistema de autenticación básico
* 🛠️ Panel de administración para gestión completa
* 🖥️ Visualización de productos en página principal
* 🔍 Vista de detalle de productos
<img width="1918" height="736" alt="pizza6" src="https://github.com/user-attachments/assets/50adee04-a27c-446d-916f-bf14dbe2308b" />

---

## 🧪 Flujo de uso

### 👤 Cliente

* Puede registrarse en la plataforma
* Visualiza las pizzas disponibles
* Accede al detalle de cada producto

### 🛠️ Administrador

* Gestiona ingredientes, masas, tamaños y pizzas
* Administra usuarios
* Controla la información del sistema

---

## ⚠️ Importante

🚧 Este proyecto **NO incluye sistema de compra o pagos**

👉 Está diseñado intencionalmente como base para que el desarrollador:

* implemente carrito de compras
* integre pasarelas de pago
* agregue lógica de negocio adicional

---

## 🧱 Tecnologías utilizadas

* Python
* Django 4.2.5
* SQLite
* HTML / CSS
* Django Crispy Forms
* Crispy Bootstrap 5
* Django Admin Interface

---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash id="9j2s8x"
git clone https://github.com/KhadaKayn/GestionLocal-Pizza.git
cd GestionLocal-Pizza
```

2. Crear entorno virtual:

```bash id="h7d3lm"
python -m venv venv
```

3. Activar entorno:
# Windows
```bash id="m4k2vd"

venv\Scripts\activate
```
# Linux / Mac
```bash id="m4k2vd"

source venv/bin/activate
```

4. Instalar dependencias:

```bash id="r8p1zf"
pip install -r requirements.txt
```

5. Ejecutar migraciones:

```bash id="c6x9qs"
python manage.py migrate
```

---

## ▶️ Ejecución

```bash id="g3z8nt"
python manage.py runserver
```

Abrir en:

```text id="t7n2qv"
http://127.0.0.1:8000/
```

---

## 🔐 Acceso inicial

```text id="y2b8mw"
Usuario: admin
Contraseña: admin
```

*(Se recomienda cambiar credenciales en producción)*

---

## 🧪 Estado del proyecto

🚧 Base funcional en desarrollo

Incluye:
<img width="1022" height="656" alt="pizza4" src="https://github.com/user-attachments/assets/4688249b-0e90-40bd-976a-710e47a48871" />
<img width="908" height="853" alt="pizza5" src="https://github.com/user-attachments/assets/54f331b9-79dd-4ad4-bd77-c08d35f003fa" />

* estructura de gestión de productos
* autenticación básica
* panel administrativo
* vistas públicas

---


---

## 👨‍💻 Autor

* Marcelo Ponce

---

## ⭐ Notas

Este proyecto está pensado como una **base reutilizable para sistemas de gestión**, aplicable no solo a pizzerías, sino a cualquier negocio que requiera administración de productos y usuarios.

---
