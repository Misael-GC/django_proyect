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

* Configurar la base de datos
* 