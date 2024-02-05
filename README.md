# Mi aplicación

El presente trabajo se realizó para un **desafío técnico**. La parte más destacada que quería resaltar son las habilidades de manejo de **Python, Django, HTML y CSS, lógica de programación y creación de modelos para presentación de datos y trabajo con bases de datos**. No por último, me gustaría agregar que gracias al presente proyecto, pude adquirir habilidades de uso y manejo de la **librería de OpenAI** para consumir los servicios de la **API de OpenAI GPT**, permitiéndome trabajar en una tarea que no es común ver en el mercado laboral.

## Instrucciones de instalación

Para instalar el proyecto, simplemente clona el repositorio en local. Utiliza el archivo **'requirements.txt'** para instalar las dependencias. No deberías necesitar migrar nada, pero puedes ejecutar el comando en terminal **'python manage.py makemigrations'** para verificar si es necesario realizar migraciones. Si es así, ejecuta **'python manage.py migrate'** finalmente inicia el servidor con **'python manage.py runserver'**. La URL se indicará en la terminal (por ejemplo, "http://127.0.0.1:8000/").

**Notas:**
- La URL del servidor puede variar; asegúrate de utilizar la correcta para evitar problemas de navegación. (Si la url es diferente no funccionara el menu de navegacion en la pagina).
- Para consumir los servicios de la API OpenAI, es necesario tener una cuenta registrada y un token de acceso válido.
- **Token de acceso OpenAI:**
  - Crea un archivo llamado ".env" en la raíz del proyecto.
  - Dentro de ".env", agrega el token de acceso de OpenAI de la siguiente manera:

    **Ubicacion del archivo**

    ![Ubicacion del archivo en la carpeta del proyecto](images\token_1.jpg)


    **Contenido del archivo**
    ![Contenido del archivo:](images\token_2.jpg)

  - Inserta tu token de acceso en lugar de "pegarlo aca" sin modificar el nombre de la variable.
  - Guarda el archivo ".env".
- La ejecución del programa incluye consultas y respuestas guardadas en la base de datos, proporcionando un historial útil.

Sobre la ejecución del programa en sí, es interesante ya que las consultas y las respuestas se guardan en la base de datos. Si haces la misma consulta, el programa revisará en la base de datos si ya existe y no llamará a la API de OpenAI. Puedes probar con una pregunta que ya esté registrada en la base de datos: **cual es la capital de Chile**. Si realizas esta consulta sin un token de acceso, creo que debería funcionar.

Se pueden implementar varias cosas más, como por ejemplo, un contador para cada consulta, así puedes hacer un análisis de las consultas y saber cómo mejorar el negocio, etc.

Decidí dejar público mi trabajo para que puedan explorarlo. Si hay algún negocio lucrativo involucrado, por favor, ten en cuenta que no me responsabilizo.

Espero que les haya gustado mi trabajo. Cualquier duda o consulta, estoy dispuesto a ayudar y apoyar en lo que pueda. También se reciben retroalimentaciones para poder mejorar.

Correo electronico: i_cucer@mail.ru

Atte. ION C.