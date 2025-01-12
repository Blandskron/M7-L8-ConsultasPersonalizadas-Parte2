# Proyecto Django - Acceso a base de datos sin modificarla

Este es un proyecto Django que se conecta a una base de datos existente sin realizar ningún cambio en ella. El objetivo es acceder y mostrar datos desde tablas ya creadas sin ejecutar migraciones ni alterar la base de datos de ninguna manera.

## Objetivo

El objetivo de este proyecto es configurar Django para leer datos desde una base de datos preexistente (sin hacer modificaciones) y mostrarlos en una página HTML. Se deshabilitaron las migraciones y la creación de nuevas tablas para evitar cambios en la base de datos. Además, se creó una vista en Django para consultar y mostrar esos datos en una página web.

## Pasos Realizados

1. **Conexión a una base de datos existente**:
   En el archivo `settings.py`, se configuró la base de datos para conectarse a una base de datos MySQL llamada `test_DB`, sin permitir la creación ni la modificación de tablas.

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'test_DB',
           'USER': 'root',
           'PASSWORD': 'admin1234',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

2. **Desactivación de migraciones**:
   Para evitar que Django intente crear o modificar tablas, se desactivaron las aplicaciones de migración relacionadas con la autenticación y el administrador de Django. Esto se logró añadiendo las siguientes líneas al archivo `settings.py`:

   ```python
   MIGRATION_MODULES = {
       'auth': None,
       'admin': None,
       'contenttypes': None,
       'sessions': None,
   }
   ```

3. **Generación de modelos a partir de la base de datos**:
   En lugar de crear modelos manualmente, utilizamos el comando `inspectdb` para generar automáticamente los modelos Django a partir de las tablas existentes en la base de datos. Esto se hace con el siguiente comando:

   ```bash
   python manage.py inspectdb > models.py
   ```

   Este comando escanea la base de datos y genera un archivo `models.py` con los modelos correspondientes a las tablas existentes.

   Después de ejecutar el comando, abre el archivo `models.py` generado y asegúrate de que los modelos tengan la configuración correcta. También puedes añadir `managed = False` para evitar que Django intente modificar esas tablas.

4. **Creación de una vista para leer los datos**:
   En `views.py`, se creó una vista para obtener todos los registros de la tabla generada por `inspectdb` y pasarlos a un template HTML para su visualización.

   ```python
   def my_table_view(request):
       rows = MyTable.objects.all()
       return render(request, 'myapp/my_table.html', {'rows': rows})
   ```

5. **Creación del template HTML**:
   Se creó un template HTML (`my_table.html`) que muestra los datos de la tabla en una tabla HTML:

   ```html
   <table border="1">
       <thead>
           <tr>
               <th>ID</th>
               <th>Nombre</th>
               <th>Correo</th>
           </tr>
       </thead>
       <tbody>
           {% for row in rows %}
           <tr>
               <td>{{ row.id }}</td>
               <td>{{ row.name }}</td>
               <td>{{ row.email }}</td>
           </tr>
           {% empty %}
           <tr>
               <td colspan="3">No hay datos disponibles</td>
           </tr>
           {% endfor %}
       </tbody>
   </table>
   ```

6. **Configuración de las URLs**:
   Se configuraron las URLs en `urls.py` para poder acceder a la vista que muestra los datos en la página web.

   ```python
   urlpatterns = [
       path('my_table/', views.my_table_view, name='my_table'),
   ]
   ```

## ¿Cómo ejecutar el proyecto?

1. **Clonar el repositorio**:
   Clona el proyecto en tu máquina local.

2. **Instalar dependencias**:
   Si aún no tienes un entorno de Django configurado, instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos**:
   Asegúrate de que la base de datos MySQL esté corriendo y configurada correctamente en `settings.py`.

4. **Generar modelos automáticamente**:
   Si aún no lo has hecho, usa el comando `inspectdb` para generar los modelos de Django a partir de la base de datos existente:

   ```bash
   python manage.py inspectdb > models.py
   ```

5. **Ejecutar el servidor de desarrollo**:
   Inicia el servidor de desarrollo de Django:

   ```bash
   python manage.py runserver
   ```

6. **Acceder a la página**:
   Abre tu navegador y ve a la URL configurada para ver los datos de la tabla en HTML:

   ```
   http://127.0.0.1:8000/my_table/
   ```

## Conclusión

Este proyecto está diseñado para acceder a datos existentes en una base de datos sin realizar cambios en la misma. Django se conecta a la base de datos, consulta los datos y los muestra en una página HTML sin intentar crear o modificar ninguna tabla.
