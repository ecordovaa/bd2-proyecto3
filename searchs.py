from rtree_index import *

def recognize_face(file, k):
    #Procesamiento de la imagen de query.
    input_img = encode_file(file)
    
    #Rtree indexado con todas las fotos de un fichero.
    #Se le puede enviar la cantidad de fotos a indexa.
    #Si no se le envia un numero, lee todas.
    #Lee tambien la imagen de input
    rtree = create_rtree_index(input_img)

    #Aplicar KNN-Rtree, colocar la lista de files en un json y mandarsela a pol