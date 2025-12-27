EJERCICIO DE RECUPERACIÓN - Sistema de Gestión de Clientes y Facturas
Desarrollo Web en Entorno Servidor - Curso 2025/2026
Duración: 2 horas | Puntuación máxima: 16 puntos


ESTRUCTURA OBLIGATORIA
text
recuperacion_tuapellido/
├── app.py
├── config.py
├── .env
├── clientes/
│   ├── __init__.py
│   └── rutas.py
├── facturas/
│   ├── __init__.py
│   └── analisis.py
├── templates/
│   ├── base.html
│   ├── clientes.html
│   ├── nueva_factura.html
│   ├── error400.html
│   ├── error404.html
│   └── analisis.html
Blueprints obligatorios: clientes_bp, facturas_bp

BLOQUE A: FLASK - GESTIÓN CLIENTES (8 puntos)
A.1 Configuración (2 puntos)
config.py debe contener:

Clase Config (base)

DevelopmentConfig: API_BASE="test.local"

ProductionConfig: SECRET_KEY y API_BASE="prod.server.com" desde .env

app.py: Carga configuración según FLASK_ENV del .env
=====================================================================
A.2 Funciones clientes_bp (4 puntos)
ver_clientes() (1.5 puntos)

Lee cookie clientes

Convierte JSON → variable clientes_lista

Renderiza clientes.html

nueva_factura() (1.5 puntos)

GET: Muestra nueva_factura.html

POST: Recibe cliente. Si vacío → abort(400)

Válido → añade a cookie clientes (10 días) → redirect(url_for('clientes_bp.ver_clientes'))

Eliminación (1 punto)

eliminar_cliente/<int:pos>: Posición inválida → abort(404)

limpiar_todos(): Borra cookie completa → redirect listado


=====================================================================

A.3 Plantillas y errores (1 punto)
text
base.html (herencia + menú con enlaces)
clientes.html (tabla clientes_lista)
nueva_factura.html (formulario cliente)
error400.html / error404.html (personalizadas)

=====================================================================
BLOQUE B: PYTHON - ANÁLISIS FACTURAS (8 puntos)
B.1 facturas/analisis.py (6 puntos)
analizar_clientes() (2 puntos)

text
datos = {
    "empresaA": [1500, 2200, 1800],
    "freelanceB": [300, 450, 600],
    "tiendaC": [800, 1200, 950]
}
Devolver:

text
{
    "ingresos": {"empresaA": 5500, "freelanceB": 1350, "tiendaC": 2950},
    "grandes": ["empresaA"],
    "creciente": "freelanceB"
}

=====================================================================
calcular_impuestos(*args, **kwargs) (2 puntos)

text
calcular_impuestos(1000, 2000, irpf=0.15, iva=0.21)
Devolver:

text
{
    "base_args": 3000,
    "porcentajes": 0.36,
    "total_tasas": 4
}

=====================================================================
seleccionar_facturas(facturas, minimo=1000, tipo="alto") (2 puntos)

text
facturas = {"F001": 800, "F002": 2500, "F003": 1200}
tipo="alto": {"F002": 2500}

tipo="bajo": {"F001": 800}
=====================================================================

B.2 Vista analisis_completo() (2 puntos)
Llama las 3 funciones

calcular_impuestos(500, 700, bonus=0.05)

seleccionar_facturas(facturas, 1500, "bajo")

Resultados → analisis.html

Enlace desde base.html

FLUJOS ESPERADOS
text
1. GET /clientes → Tabla clientes_lista (cookie)
2. POST /nueva_factura cliente="" → error400.html
3. GET /eliminar_cliente/999 → error404.html  
4. GET /analisis_completo → Resultados Python