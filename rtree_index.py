import face_recognition as fr
from rtree import index
from os import listdir
from sklearn.descomposition import PCA

def encode_file(file):
    img = fr.load_image_file(file)
    res = fr.face_encodings(img)
    if(len(res) > 0):
        return res[0]
    return [0] * 128

def create_rtree_index(n = 13234):
    p = index.Property()
    p.dimension = 128
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index('rtree_index', properties=p)
    i = 0
    for img in listdir('fotos_bd/'):
        print(i)
        print(img)
        idx.insert(i, tuple(encode_file(f'fotos_bd/{img}')))
        i += 1
    idx.close()