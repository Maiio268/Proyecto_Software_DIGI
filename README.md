# Descripción del proyecto
El proyecto consiste en la creación de un software que crea y modifica horarios escolares semanales sin que existan conflictos, esto se desarrolla con un archivo Python que incluye todo el código necesario y, respecto a la interacción con el usuario, se ha creado un bot de telegram a través del cual el usuario puede crear y eliminar estos horarios.

# ¿Qué hace el código?
El código Python del archivo codigo_sistema.py hace lo siguiente:
Permite a los usuarios gestionar un de manera sencilla. Los usuarios pueden agregar, visualizar y eliminar horarios mediante comandos de Telegram. El bot almacena la información en una base de datos SQLite y organiza las materias respetando los horarios y un recreo.
Los comandos existentes en el código son los siguientes:
- /start: Muestra un mensaje de bienvenida con los comandos disponibles.
- /agregar_horario: Permite ingresar días, materias y aulas.
- /ver_horarios: Muestra el horario que el usuario haya creado en forma de tabla.
- /eliminar_horarios: Borra todos los horarios creados por el usuario.

# ¿Cómo probarlo?
1) Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
cd Proyecto_Software_DIGI
```
2) Instalar dependencias:

```
pip install -r requirements.txt
```

3) Ejecutar el bot:
Para ejecutar el bot, abre la terminal y escribe el siguiente comando:
```
python codigo_sistema.py
```
IMPORTANTE: Asegurate que estás posicionado en la carpeta del proyecto.

4) Ahora inicia sesión con tu cuenta en Telegram y escribe en el buscador (posicionado en la parte superior de la pantalla de la aplicación Telegram) el nombre del bot: SmartHorarioBot.

5) Ahora ya puedes interactuar con el bot usando los comandos disponibles.

