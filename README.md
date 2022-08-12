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
