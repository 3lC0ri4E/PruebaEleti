# Mini API de Tareas

## Descripción General
Sistema completo de gestión de tareas con backend API REST usando Django REST Framework y frontend interactivo en HTML/JavaScript. Incluye autenticación de sesión, CRUD completo y interfaz responsiva.

## Tecnologías Utilizadas

### Backend
- **Framework**: Django 5.2.7
- **API**: Django REST Framework
- **Autenticación**: Token Authentication (DRF authtoken)
- **Base de Datos**: SQLite3
- **CORS**: django-cors-headers para permitir solicitudes del frontend

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Diseño responsivo con gradientes y animaciones
- **JavaScript**: Vanilla JS con Fetch API
- **Almacenamiento**: localStorage para persisti token
- **Características**: Actualización automática cada 2 segundos

## Requisitos Cumplidos

### 1. API REST Funcional ✓
- **GET** `/api/tasks/` - Listar todas las tareas del usuario autenticado
- **POST** `/api/tasks/` - Crear nueva tarea
- **PATCH** `/api/tasks/{id}/` - Actualizar estado de tarea (completada/pendiente)
- **DELETE** `/api/tasks/{id}/` - Eliminar tarea

### 2. Campos de Tarea ✓
- `id`: Identificador único (auto-generado)
- `nombre`: Nombre descriptivo de la tarea (máx 200 caracteres)
- `completada`: Boolean que indica si la tarea está completada
- `fecha_de_creacion`: Timestamp automático

### 3. Autenticación ✓
- Token Authentication requerida
- Endpoint de login: `POST /api/login/`
- Solo usuarios autenticados pueden acceder a las tareas
- Las tareas se filtran por usuario (cada usuario ve sus propias tareas)
- Token almacenado en localStorage del navegador
- Formulario de login integrado en el frontend

### 4. Tabla de Datos ✓
- Tabla HTML dinámica que muestra las tareas en tiempo real
- Actualización automática cada 2 segundos
- Botones para completar/descomentar tareas
- Botón para eliminar tareas
- Estado visual (Completada/Pendiente) con colores diferenciados
- Mensaje "No hay tareas" cuando lista está vacía
- Responsive design para móviles

### 5. Entregables ✓
- Repositorio público con estructura clara
- Este README.md con documentación completa
- Código bien organizado y comentado

## Estructura del Proyecto

```
PruebaEleti/
├── frontend/
│   └── index.html                    # Interfaz de usuario
├── mini_api/                         # Backend Django
│   ├── manage.py
│   ├── db.sqlite3                    # Base de datos
│   ├── mini_api/
│   │   ├── settings.py              # Configuración Django
│   │   ├── urls.py                  # Rutas principales
│   │   └── wsgi.py
│   ├── tasks/                        # App de tareas
│   │   ├── models.py                # Modelo Task
│   │   ├── serializers.py           # Serializador DRF
│   │   ├── views.py                 # ViewSet
│   │   ├── urls.py                  # Rutas API
│   │   └── migrations/
│   └── venv/                         # Virtual environment
└── README.md                         # Este archivo
```

## Instalación y Ejecución

### Backend

1. Navega al directorio del backend:
```bash
cd mini_api
```

2. Crea y activa el virtual environment (si no existe):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Aplica migraciones:
```bash
python manage.py migrate
```

5. Crea superusuario (para panel admin):
```bash
python manage.py createsuperuser
```

6. Inicia servidor de desarrollo:
```bash
python manage.py runserver
```

El backend estará disponible en `http://127.0.0.1:8000/`

### Frontend

1. Abre el archivo `frontend/index.html` en tu navegador
2. El frontend se conectará automáticamente a `http://127.0.0.1:8000/api/tasks/`

## Flujo de Uso

### Primer uso
1. Abre el frontend
2. Verás formulario de login
3. Ingresa tus credenciales (usuario y contraseña)
4. Haz clic en "Entrar"

### Con autenticación
1. El token se guardará en localStorage
2. Verás: "Conectado al servidor - Autenticado"
3. Ahora puedes:
   - Crear tareas escribiendo nombre + botón "Crear Tarea"
   - Completar/descompletar tareas con botón "Completar/Pendiente"
   - Eliminar tareas con botón "Eliminar"
   - Las tareas se actualizan automáticamente cada 2 segundos

### Logout
1. Haz clic en "Cerrar Sesión"
2. El token se borra del localStorage
3. Vuelves al formulario de login

## Detalles de Implementación

### Backend (Django)

**Modelo Task** (`tasks/models.py`):
```python
- usuario: ForeignKey(User) - Relaciona la tarea con el usuario propietario
- nombre: CharField (máx 200)
- completada: BooleanField (default=False)
- fecha_de_creacion: DateTimeField (auto_now_add)
```

**Serializer** (`tasks/serializers.py`):
- Convierte el modelo a/desde JSON
- Solo campos legibles: id, fecha_de_creacion, usuario
- Campos editables: nombre, completada

**ViewSet** (`tasks/views.py`):
- Implementa CRUD completo
- Requiere autenticación (IsAuthenticated)
- `get_queryset()`: Filtra tareas por usuario autenticado
- `perform_create()`: Asigna automáticamente el usuario al crear
- Ordena por fecha de creación (más recientes primero)

**Autenticación** (`mini_api/settings.py`):
```python
DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
]
DEFAULT_PERMISSION_CLASSES = [
    'rest_framework.permissions.IsAuthenticated',
]
```

**Endpoint de Login** (`mini_api/urls.py`):
```python
path('api/login/', obtain_auth_token, name='api_token_auth'),
```

### Frontend (HTML/JS)

**Características principales**:
- Fetch API con header `Authorization: Token {token}`
- Token guardado en localStorage para persistencia
- Detección automática de errores 401 (no autenticado)
- Validación de entrada
- Escapado de caracteres HTML para seguridad
- Actualización automática cada 2 segundos
- Diseño responsivo
- Formulario de login mejorado con labels

## Estados de Conexión

El frontend muestra diferentes estados:

| Estado | Significado |
|--------|------------|
| Conectado al servidor - Autenticado | Sesión activa, tareas visibles |
| No autenticado | No hay sesión iniciada |
| Error de conexión | Servidor no disponible |
| Error: [status] [code] | Error específico de API |

## Seguridad

✓ **Implementado**:
- Autenticación de sesión requerida
- CORS configurado
- Escapado de HTML en frontend
- Validación de entrada
- CSRF protection

## API Endpoints

### Listar/Crear Tareas
```
GET/POST http://127.0.0.1:8000/api/tasks/
Requiere: Autenticación
```

### Detalle/Actualizar/Eliminar
```
GET/PATCH/DELETE http://127.0.0.1:8000/api/tasks/{id}/
Requiere: Autenticación
```

### Panel Administrativo
```
http://127.0.0.1:8000/admin/
```

### API Browsable
```
http://127.0.0.1:8000/api/tasks/
```

## Notas de Desarrollo

- El servidor de desarrollo Django debe estar corriendo para que funcione
- Las cookies de sesión se mantienen en el navegador
- Cada usuario solo ve sus propias tareas
- La base de datos SQLite se crea automáticamente en la primera ejecución
- El frontend se actualiza cada 2 segundos para detectar cambios
