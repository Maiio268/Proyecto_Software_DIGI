# Descripción del proyecto
El proyecto consiste en la creación de un software que crea y modifica horarios escolares semanales sin que existan conflictos, esto se desarrolla con un archivo Python que incluye todo el código necesario y, respecto a la interacción con el usuario, se ha creado un bot de telegram a través del cual el usuario puede crear y modificar estos horarios.

# Preguntas a responder:
## Ciclo de vida del dato
1) ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
Los datos se crean cuando el usuario introduce las materias aulas... y estos datos se almacenan en una base de datos SQLite. El usuario puede consultar los datos de los horarios que están en la base de datos con el comando /ver_horarios, también puede eliminar todos los horarios con el comando /eliminar_horarios, que elimina todos los registros del usuario.
2) ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
Se asegura que los datos ingresados por el ususario sean válidos. Además, cada horario tiene un identificador único y los datos se almacenan en la base de datos en un formato perfectamente estructurado.
## Almacenamiento en la nube 
1) Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
El proyecto no usa la nube, pero en un futuro podría utilizarse Google Firebase o una base de datos que esté en la nube, como PostgreSQL o MySQL. También se podría modificar el proyecto de forma que se conecte con Google Drive y los usuarios puedan ver sus respectivos horarios desde cualquier dispositivo utilizando su cuenta de Google Drive.
## Seguridad y regulación
1) ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
La seguridad se gestiona mediante el almacenamiento local de los horarios en una base de datos SQLite. Los datos de cada usuario se diferencian mediante el ID de Telegram de cada usuario, esto evita que se provoque el acceso no autorizado a la información sobre los horarios de otros usuarios. No se guardan contraseñas ni informazión personal para minimizar los riesgos de filtración.
2) ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?
Mi software no maneja información sensible de los usuarios que lo utilizan, por lo que las normativas GDPR no podrían afectar el uso del mismo, aunque si mi bot manejase información personal de los usuarios añadiría una política de privacidad la cual informa a los usuarios sobre los datos personales que se almacenan y cómo pueden ser eliminados.
## Implicación de las THD en negocio y planta
1) ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?
En un entorno escolar/académico, el bot facilitaría la organización de los horarios de clases ya sea para estudiantes o profesores, en un entorno empresarial es lo mismo, puede facilitar la gestión de reuniones o turnos de trabajos.
2) ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
El bot permite crear horarios, evitando así errores humanos en la organización, además, facilita el acceso rápido a la información de los horarios escribiendo un simple comando, así, la toma de decisiones se convierte en una tarea mucho más sencilla, al igual que los procesos operativos.
## Mejoras en IT y OT
1) ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?
El bot digitaliza un proceso que se hace normalmente de forma manual, esto permite acceso instantáneo y almacenamiento seguro, por esta parte IT está cubierto. Además, el software puede ser utilizado en entornos educativos o empresariales para automatizar la planificación de horarios usando una interfaz sencilla e intuitiva, de esta forma OT se integra correctamente.
2) ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?
- Planificación de horarios automatizada: Permite que los estudiantes y profesores ingresen y consulten horarios fácilmente desde un bot de Telegram, sin necesidad de consultar documentos físicos o archivos dispersos que no están claramente ordenados en un lugar.
- Gestión centralizada de datos: Los datos de los horarios se almacenan en una base de datos SQLite, asegurando que la información esté organizada y accesible en cualquier momento.
- Optimización del tiempo: Permite a los usuarios ver su horario completo de la semana en formato de tabla, lo que facilita la visualización de los datos a los usuarios ya que se pueden visualizar de una forma fácil e intuitiva, esto ahorra tiempo en la consulta del usuario.
## Tecnologías Habilitadoras Digitales