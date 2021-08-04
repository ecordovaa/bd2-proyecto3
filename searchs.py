from rtree_index import *

def recognize_face(file, k):
    #Procesamiento de la imagen de query.
    input_img = encode_file(file)
    print(len(input_img))
    
    #Rtree indexado con todas las fotos de un fichero.
    #Se le puede enviar la cantidad de fotos a indexa.
    #Si no se le envia un numero, lee todas.
    #Lee tambien la imagen de input

    #Aplicar KNN-Rtree, colocar la lista de files en un json y mandarsela a pol

    return 'La foto del archivo se leyo correctamente.'