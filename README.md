# Instrucciones para crear un proyecto en Django e inicio de proyecto

* Crear el entorno: https://misael-gomez-cuautle.super.site/blog-personal-1/projects/entorno-virtual-en-python
* pip install django 
* django-admin startproject erp 
* cd erp
* py manage.py startapp tools: crear un nuevo modulo
* pip install djangorestframework

Ir a settings.py de la carpeta principal

```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'tools' # add my folder/app - help with the migrations,
]

```

* Configurar la base de datos settings.py
se puede hacer un .env, pero en este caso es un proyecto de ejemplo

```py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### Hcemos que sea mexicano
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True
```

Instalamos esto para no tener errores con postgres
```bash

pip install psycopg2-binary

pip freeze > requirements.txt

```

Ya trabajamos sobre la aplicacion tools

## Creacion de Modelos de BD

models.py

Se integra la clase con la estructura del modelo, revisa el archivo.

corremos el siguiente comando para migrar

```
py manage.py makemigrations

py manage.py migrate

```

----
### Si descargas de github
Si ya todo esta listo hasta aquí solo arrancas  env entorno virtual
entras al proyecto y ejecutas

```bash
pip install -r requirements.txt
py manage.py migrate
```

-----

* se crea la carpeta api/serilizer.py, views.py, urls.py  y ahí puedes ver la logica
* En urls.py del folder principal, en este caso erp, agregamos a urlpapatterns
    - Incluye las URLs de la API de herramientas
  

  ```py
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tools.api.urls')),  # Incluye las URLs de la API de herramientas
]

  ```


### Proximos pasos

```bash
py manage.py createsuperuser
```
* pon un nombre como admin
* correo y contraseña

corre el siguiente comando

```bash
py manage.py runserver
```

Entras a /admin y puedes entrar al dashboard

en la carpeta tools/admin.py

Recarga la pagina y ya lo obtendras

y despues de rtegistrar una nueva herramienta 
ve a localhost:8000/api y veras ahi la url

haz pruebas con POSTMAN


----
checar erp>settings.py

Permite los links que pueden entrar
```py
# CORS_ORIGIN_ALLOW_ALL = ['*']
```