# Pixelar Brief Hub

Proyecto final de Python / Django – Comisión 78130 Playground  
Autor: **Cristian Javier Ruiz (Studio Pixelar)**

Pixelar Brief Hub es una aplicación web tipo blog/panel interno para **gestionar briefs de proyectos reales de Studio Pixelar**, junto con un módulo de **usuarios, perfiles y mensajería interna**.  
La app cumple con los requisitos del trabajo final (home, about, pages, auth, perfil, CRUD completo, mensajes, CBV + mixins, etc.) y está pensada para ser escalable y reutilizable en el día a día de la agencia.

---

## Tecnologías principales

- **Python 3.12**
- **Django 5.x**
- **SQLite** (desarrollo)
- **Tailwind CSS v4 (CLI)** para la UI
- **CKEditor** para texto enriquecido en los briefs
- HTML semántico + templates con herencia (`base.html`)

---

## Estructura general

- `pixelar_hub/` – Configuración principal de Django (settings, urls, wsgi).
- `core/` – Páginas generales:
  - Home (`/`)
  - About (`/about/`)
  - Template base con navbar, mensajes y layout.
- `briefs/` – App principal (modelo `Brief`):
  - Listado de pages (`/pages/`)
  - Detalle de page
  - Crear / editar / borrar (solo usuarios logueados).
- `accounts/` – Usuarios y autenticación:
  - Signup, Login, Logout
  - Perfil, edición de perfil, cambio de contraseña.
- `messaging/` – Mensajería interna entre usuarios:
  - Bandeja de entrada, enviados, detalle, enviar mensaje.
- `static/`
  - `src/input.css` – entrada de Tailwind.
  - `css/styles.css` – CSS generado por Tailwind.
- `media/` – Archivos subidos (avatars, imágenes de briefs) – **no se sube al repo**.
- `templates/` – Distribuidos por app, todas heredan de `core/base.html`.

---

## Requisitos previos

- Python 3.12 instalado.
- Node.js (para compilar Tailwind).
- Git.

---

## Instalación y puesta en marcha

1. **Clonar el repositorio**

   ```bash
        git clone https://github.com/PixelarStudio/studio_pixelar_brief_hub_Cruiz.git
        cd studio_pixelar_brief_hub_Cruiz
   ```
2. **Crear y activar entorno virtual**
   ```bash
        python -m venv .venv
        .venv\Scripts\activate # Windows
   ```

3.  **Instalar dependencias de Python**
   ```bash
        pip install --upgrade pip
        pip install -r requirements.txt
```
4.  **Instalar dependencias de Node (Tailwind)**
   ```bash
        npm install
   ```

5.  **Compilar Tailwind CSS**

    En una terminal aparte (dejar corriendo en desarrollo):
   ```bash
        npx @tailwindcss/cli -i ./static/src/input.css -o ./static/css/styles.css --watch
   ```

6.  **Aplicar migraciones**
   ```bash
        python manage.py migrate
   ```

7.  **Crear superusuario para admin**
   ```bash
        python manage.py createsuperuser
   ```

8.  **Ejecutar el servidor**
   ```bash
         python manage.py runserver
   ```

    Abrir en el navegador:  
    `http://127.0.0.1:8000/`

---

## Uso de la aplicación

### Sin autenticación (modo lectura)

- **Home** (`/`): **Inicio** presentación de Pixelar Brief Hub.
- **About** (`/about/`): **Acerca de Mi** información sobre el autor y el objetivo del proyecto.
- **Pages** (`/pages/`): **Proyectos**
  - Listado de briefs (modelo `Brief`).
  - Vista de detalle al hacer clic en “Leer más”.
  - Si no hay pages o la búsqueda no devuelve resultados, se muestra el mensaje  
    **“No hay páginas aún”** (o equivalente de “sin resultados”).

### Con usuario autenticado

Una vez logueado, se habilitan las acciones de gestión.

#### Pages / Briefs

- **Crear nueva page** (brief).
- **Editar** una page existente.
- **Eliminar** una page existente.
- Solo usuarios logueados pueden crear/editar/borrar (uso de `LoginRequiredMixin`).

Cada `Brief` contiene:

- `title` – título del proyecto.
- `client_name` – cliente / marca.
- `service_type` – tipo de servicio (Portfolio, Web corporativa, E-commerce, etc.).
- `body` – descripción/brief en texto enriquecido (CKEditor).
- `reference_image` – imagen de referencia del proyecto.
- `created_at` – fecha de creación.
- `owner` – usuario que cargó el brief.

Los briefs que cargues pueden basarse en **proyectos reales** del portfolio de Studio Pixelar (San Isidro Policlínica Privada, Studio Pixelar, Ruba Tecno, Sempre A Full), adaptados para este panel interno.

#### Cuentas y perfil (`accounts`)

- **Signup**: registro de usuarios con `username`, `email` y `password`.
- **Login / Logout**: autenticación estándar de Django.
- **Profile**:
  - Nombre
  - Apellido
  - Email
  - Avatar
  - Bio
  - Website
  - Fecha de nacimiento
- **Editar perfil**: modificación de los datos anteriores (incluye subir avatar).
- **Cambiar contraseña**: formulario de cambio de contraseña con validación.

#### Mensajería interna (`messaging`)

- **Inbox**: bandeja de entrada con mensajes recibidos.
- **Enviados**: mensajes enviados por el usuario.
- **Detalle de mensaje**: vista completa de un mensaje concreto.
- **Nuevo mensaje**: formulario para enviar un mensaje a otro usuario registrado.

---

## Panel de administración

Django admin está habilitado en `/admin/`.

Desde allí se puede:

- Gestionar usuarios y grupos.
- Gestionar briefs (`Brief`).
- Gestionar perfiles (`Profile`).
- Gestionar mensajes (`Message`).

---

## Requisitos de la consigna y cómo se cumplen

- Home y About: ✔
- NavBar con accesos a Inicio / Acerca de Mi / Proyectos / Login / Registrarse / Perfil / Mensajes: ✔
- Modelo principal con:
  - 2 `CharField`.
  - 1 campo de texto enriquecido (CKEditor).
  - 1 campo de imagen.
  - 1 campo de fecha. ✔
- Listado de objetos del modelo principal con acceso a detalle: ✔
- Mensaje cuando no hay objetos o no hay resultados en la búsqueda: ✔
- CRUD completo (create / update / delete) solo para usuarios logueados: ✔
- App `accounts` para manejo de login, logout, registro y perfil: ✔
- Perfil con avatar, bio, link y datos de usuario + vista de edición + cambio de password: ✔
- App de mensajería para comunicación entre usuarios: ✔
- Mínimo 2 vistas basadas en clases (CBV): ✔ (List, Detail, Create, Update, Delete en `briefs`).
- Mínimo 1 mixin (`LoginRequiredMixin`) y 1 decorador (`@login_required`): ✔
- Herencia de templates con `base.html` y navbar: ✔
- `requirements.txt` actualizado: ✔
- `.gitignore` excluyendo `__pycache__`, `db.sqlite3`, `media`, `.venv`, `node_modules`: ✔

---

## Notas finales

Este proyecto se basa en proyectos reales del portfolio de Studio Pixelar y se desarrolló como trabajo final de la cursada de Python/Django.
