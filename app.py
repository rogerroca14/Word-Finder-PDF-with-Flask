import os
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import pandas as pd

app = Flask(__name__)

# Funcion para normalizar
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("\n", " ")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# Funcion para convertir pdf a txt
def convert_pdf_to_text(doc_pdf,id):
    from io import StringIO
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser

    output_string = StringIO()
    with open(doc_pdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    with open(("archivos_txt/file-text-" + str(id) + ".txt"), "w") as txtfile:
        print("String Variable: {}".format(normalize(output_string.getvalue().lower())), file=txtfile)

# Conección con MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registro_archivos'
mysql = MySQL(app)

# Configuraciones para session
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM archivos_pdf')
    data = cur.fetchall()
    return render_template('index.html', archivos_pdf = data)

### Funciones de importar
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './archivos_pdf'

@app.route("/")
def upload_file():
    # renderiamos la plantilla "formulario.html"
    return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        print(filename)

        # Convirtiendo el PDF a txt
        cur = mysql.connection.cursor()
        cur.execute('SELECT MAX(id_archivo) FROM archivos_pdf;')
        id_archiv = cur.fetchall()[0][0] + 1
        print(id_archiv)
        print('owo')

        # Guardamos el archivo en el directorio "archivos_pdf"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], "file-pdf-" + str(id_archiv) + ".pdf"))
        print('Empezamos rey uwu')
        convert_pdf_to_text('archivos_pdf/' + "file-pdf-" + str(id_archiv) + ".pdf", id_archiv)
        print("lo logramos nya nya")

        # Guardar en base de datos
        nombre_archivo = filename
        ruta_pdf = 'archivos_pdf/' + filename
        ruta_text = "archivos_txt/file-text-" + str(id_archiv) + ".txt"

        # Conectando a una base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO archivos_pdf (nombre_archivo, ruta_pdf	, ruta_text) VALUES (%s, %s, %s)',
        (nombre_archivo, ruta_pdf, ruta_text))
        mysql.connection.commit()

        # Retornamos una respuesta satisfactoria
        flash('Archivo ' + filename +' subido exitosamente')
        return redirect(url_for('Index'))

###

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


@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        """, (fullname, email,phone, id))
        mysql.connection.commit()
        flash('Contacto actualizado satisfactoriamente')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM archivos_pdf WHERE id={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Removido Satisfactoriamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)