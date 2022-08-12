# Funciones del programa
- Subir archivos PDF a un directorio local (o en hosting si se hace la migración correspondiente) registrando el nombre del archivo, la fecha y hora de subida además de su contenido del PDF en formato texto a una base de datos.
- Buscar una palabra u oración (menos eficiente en este caso) dentro de todos los PDF’s que hayan sido subidos previamente además de poder visualizar su contenido como PDF completo con un click o eliminarlo de nuestra biblioteca permanentemente.

![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture9.png)

### Realizar una busqueda
Digitar en el campo de la página inicial nuestra palabra a querer ubicar dentro los que tengamos registrados y dar click en “Buscar entre mis archivos”. Obtendremos como resultado un listado con los archivos que hayan coincidido con la petición, donde visualizaremos el contenido de texto del pdf referenciado completo, así como un botón para ver el PDF completo o eliminarlo.

![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture8.png)

# Instalación

1. Requisitos previos:
    - Python (3.1 o superior)
    - Navegador web de tu preferencia (Opera, Chrome, Edge, etc.)

2. Crear la base de datos con las variables:
    -	id archivo (int)
    -	nombre_archivo (varchar)
    -	fecha_hora subida (datetime)
    -	ruta_pdf (varchar)
    -	ruta_txt (varchar)
    -	contenido (longtext)
    
    ```sql
    CREATE TABLE `archivos_pdf` (`id_archivo`int(11) NOT NULL
    `nombre_archivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
    `fecha_hora_subida` datetime NOT NULL,
    `ruta_pdf` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
    `ruta_text` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
    `contenido` longtext COLLATE utf8_unicode_ci NOT NULL COMMENT 'Cadena de texto contenida en el PDF'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
    ```
3.	Descargar contenido del repositorio:
    [Github - Word-Finder-PDF-with-Flask.](https://github.com/rogerroca14/Word-Finder-PDF-with-Flask)
    
    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture1.png)

4.	Extraemos el contenido en una carpeta

    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture2.png)

    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture3.png)

5.	Ejecutar CMD en la carpeta extraída (Shift + Click Derecho en el espacio vacío)

    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture4.png)

6.	Ejecutar en la terminal el siguiente código:
    
    ```bash
    python -m pip install -r requirements.txt
    ```
    
    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture5.png)
    
    Se instalará las librerías necesarias para Python.

7.	En la misma consola ejecutar nuestro archivo app.py con el código:
    
    ```bash
    python app.py
    ```

    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture6.png)

    Copiar la ruta http://127.0.0.1:3000 y pegarla en la ruta del navegador (Esta puede variar dependiendo del equipo, el puerto se puede editar en el código del archivo app.py)

8.	Ya podemos visualizar la interfaz
    
    ![](https://raw.githubusercontent.com/rogerroca14/Word-Finder-PDF-with-Flask/master/img/Picture7.png)