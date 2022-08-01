# Librerias
import os
import datetime
import pandas as pd
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

# Funcion para normalizar (tildes y espacios dobles)
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("\n", " "),
        ("  ", " ")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# Función para convertir pdf a txt
def convert_pdf_to_text(doc_pdf,id):
    from tika import parser
    file = doc_pdf
    file_data = parser.from_file(file)
    text = normalize(file_data['content'])
    return text.encode('utf-8') # Convirtiendo a UTF-8

# Conección con MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registro_archivos'
mysql = MySQL(app)

# Configuraciones para session
app.secret_key = 'mysecretkey'

# Imprimir tabla con los valores de la base de datos
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM archivos_pdf')
    data = cur.fetchall()
    return render_template('index.html', archivos_pdf = data)

# Definiendo la Carpeta de subida para los archivos PDF
app.config['UPLOAD_FOLDER'] = './archivos_pdf'

@app.route("/")
def upload_file():
    # renderiamos la plantilla "formulario.html"
    return render_template('formulario.html')

# Ruta para subir los documentos PDF
@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # Obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        print(filename)

        # Convirtiendo el PDF a txt
        cur = mysql.connection.cursor()
        cur.execute('SELECT MAX(id_archivo) FROM archivos_pdf;')
        id_archiv = cur.fetchall()[0][0] + 1
        print(id_archiv)

        # Guardamos el archivo en el directorio "archivos_pdf"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], "file-pdf-" + str(id_archiv) + ".pdf"))

        txt_temp = convert_pdf_to_text('archivos_pdf/' + "file-pdf-" + str(id_archiv) + ".pdf", id_archiv).lower()
        fecha_temp = datetime.datetime.now()

        # Guardar en base de datos
        nombre_archivo = filename
        ruta_pdf = "archivos_pdf/file-pdf-" + str(id_archiv) + ".pdf"
        ruta_text = "archivos_txt/file-text-" + str(id_archiv) + ".txt"

        # Conectando a una base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO archivos_pdf (nombre_archivo, fecha_hora_subida, ruta_pdf , ruta_text, contenido) VALUES (%s, %s, %s, %s, %s)',
        (nombre_archivo, fecha_temp, ruta_pdf, ruta_text, txt_temp))
        mysql.connection.commit()
        txt_temp=''
        fecha_temp=''

        # Retornamos una respuesta satisfactoria
        flash('Archivo ' + filename +' subido exitosamente')
        return redirect(url_for('Index'))

# Función para añadir contactos a la pagina (TEST)
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        # Conectando a una base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname,phone,email))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('Index'))

# Ruta para eliminar un archivo
@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM archivos_pdf WHERE id_archivo={0}'.format(id))
    mysql.connection.commit()
    flash('Archivo Removido Satisfactoriamente de la carpeta contenedora')
    return redirect(url_for('Index'))

@app.route('/search/')
def about():
    return render_template('search.html')

# Definiendo sesion y puerto de sv
if __name__ == '__main__':
    app.run(port=3000, debug=True)