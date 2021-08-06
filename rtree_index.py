import face_recognition as fr
from rtree import index
import numpy as np
from os import listdir
from sklearn.decomposition import PCA

def encode_file(file):
    img = fr.load_image_file(file)
    res = fr.face_encodings(img)
    if(len(res) > 0):
        return res[0]
    return [0] * 128

def create_rtree_index(n):
    p = index.Property()
    p.dimension = 128
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index('rtree_index', properties=p)
    encodings = np.empty(shape=2)
    for img in listdir('temp/'):
        encodings += encode_file(f'temp/{img}').reshape(-1,1)
    p = PCA(n_components=1, whiten=True)
    p.fit_transform(encodings)
    for i in range(n):
        idx.insert(i, tuple(encodings[i]))
    idx.close()