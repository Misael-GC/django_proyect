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
