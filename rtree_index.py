import face_recognition as fr
from rtree import index
from os import listdir

def encode_file(file):
    img = fr.load_image_file(file)
    return fr.face_encodings(img)

def create_rtree_index(input_enc, n = 13234):
    p = index.Property()
    p.dimension = 128
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index('rtree_index', properties=p)
    i = 0
    for img in listdir('fotos_bd'):
        temp = encode_file(img)
        print(temp)
        idx.insert(i, encode_file(img))
        i += 1
    return idx