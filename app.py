# Librerias
import os
from os import remove
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

# Función para convertir pdf a texto
def convert_pdf_to_text(doc_pdf,id):
    from tika import parser
    file = doc_pdf
    file_data = parser.from_file(file)
    text = normalize(file_data['content'])
    return text.encode('utf-8') # Convirtiendo a UTF-8

# Conección con MYSQL
app.config['MYSQL_HOST'] = '50.31.188.40'
app.config['MYSQL_USER'] = 'yvalpqfp_roger_test'
app.config['MYSQL_PASSWORD'] = 'nju30xnv5xib'
app.config['MYSQL_DB'] = 'yvalpqfp_sgbd1_test'
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
app.config['UPLOAD_FOLDER'] = './static/pdf'

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

        # Guardamos el archivo en el directorio "static/pdf/"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], "file-pdf-" + str(id_archiv) + ".pdf"))

        txt_temp = convert_pdf_to_text('static/pdf/' + "file-pdf-" + str(id_archiv) + ".pdf", id_archiv).lower()
        fecha_temp = datetime.datetime.now()

        # Guardar en base de datos
        nombre_archivo = filename
        ruta_pdf = "static/pdf/file-pdf-" + str(id_archiv) + ".pdf"
        ruta_text = "static/txt/file-text-" + str(id_archiv) + ".txt"

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

@app.route('/search-results')
def searchresults():
    return render_template('search-results.html')

@app.route('/integrantes')
def integrantes():
    return render_template('integrantes.html')

@app.route('/', methods=['POST'])
def my_form_post_search():
    text = request.form['text_search_web']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from archivos_pdf WHERE contenido LIKE '%" + str(normalize(text)) +"%'")
    data_search = cur.fetchall()
    return render_template('search-results.html', data2=data_search, textsearch="Palabra buscada: '" + normalize(text) + "'")

# Ruta para eliminar un pdf de la base de datos
@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM archivos_pdf WHERE id_archivo={0}'.format(id))
    print(id)
    mysql.connection.commit()
    remove("static/pdf/file-pdf-{0}.pdf".format(id))
    flash('Archivo Removido Satisfactoriamente')
    return redirect(url_for('Index'))

# Definiendo sesion y puerto de sv
if __name__ == '__main__':
    app.run(port=3000, debug=True)