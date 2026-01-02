Aplicación web Flask modular para gestionar biblioteca digital con autenticación de usuarios y CRUD de libros usando Blueprints y cookies JSON.

Funcionalidades Implementadas
Autenticación (cliente_bp)
✅ Login con validación usuario/contraseña (datos hardcodeados)

✅ Registro de nuevos usuarios

✅ Cookie cliente=nombre (7 días persistencia)

✅ Cerrar sesión (eliminar cookie)

Gestión Libros (libros_bp)
✅ Mostrar lista libros (protegida, requiere login)

✅ Añadir libro con título + descripción (evita duplicados)

✅ Borrar libro por título

✅ Persistencia en cookie JSON libros=[{titulo, descripcion}]

Características Técnicas
text
- Blueprints modulares: cliente_bp + libros_bp
- Configuración por entornos (Development/Testing/Production)
- Manejo errores 401/403/500 con template personalizado
- Templates con herencia base.html
- Protección rutas: abort(401) sin cookie cliente
- Rutas protegidas solo accesibles tras login
Estructura del Proyecto
text
├── app.py           # App principal + registro blueprints
├── config.py        # Configuraciones entornos
├── clientes/rutas.py # Login, registro, logout
├── libros/rutas.py  # CRUD libros
└── templates/       # HTML con Jinja2
    ├── base.html
    ├── error.html
    ├── login.html
    └── libros/
        ├── catalogo.html
        ├── añadir.html
        └── borrar.html

| Ruta              | Descripción         | Método  | Autenticación |
|-------------------|---------------------|---------|---------------|
| `/`               | Redirige a login    | GET     | -             |
| `/login`          | Formulario login    | GET/POST| No            |
| `/registrar`      | Registro usuario    | GET/POST| No            |
| `/cerrar_sesion`  | Logout              | GET     | Sí            |
| `/mostrar`        | Lista libros        | GET     | **Sí**        |
| `/libros`         | Añadir libro        | GET/POST| **Sí**        |
| `/borrar`         | Borrar libro        | GET/POST| **Sí**        |
