import re
from flask import Flask, jsonify, request, redirect
from searchs import recognize_face
from rtree_index import *

app = Flask(__name__)

def allowed_file(filename):
    extension = filename.rsplit('.', 1)
    return len(extension) == 2 and extension[1] == 'jpg'

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        #No se envio ninguna imagen
        if 'file' not in request.files:
            return redirect(request.url)

        for _, value in request.form.items():
            k = int(float(value))

        #El numero de elementos a buscar esta fuera de rango
        if k <= 0 or k > 13234:
            return redirect(request.url)

        file = request.files['file']

        #Existe la imagen, pero no tiene nombre
        if file.filename == '':
            return redirect(request.url)

        #Existe la imagen y tiene alguna extension valida
        if file and allowed_file(file.filename):
            return recognize_face(file, k)

    #Si es GET o la imagen no es valida, carga de nuevo la pag de inicio
    return '''
    <!doctype html>
    <title>RECONOCIMIENTO FACIAL</title>
    <h1>Cargue un archivo de imagen e ingrese el número de personas más parecidas a la imagen que desa obtener.</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="number" step="1" pattern="\d+" name="k">
      <input type="submit" value="Cargar">
    </form>
    '''

if __name__ == "__main__":
    create_rtree_index(50)
    app.run(host='0.0.0.0', port=8080, debug=True)