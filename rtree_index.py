import face_recognition as fr
from rtree import index
from os import listdir
from sklearn.decomposition import PCA

def encode_file(file):
    img = fr.load_image_file(file)
    res = fr.face_encodings(img)
    if(len(res) > 0):
        return res[0]
    return [0] * 70

def create_rtree_index(n = 13234):
    p = index.Property()
    p.dimension = 128
    p.dat_extension = 'data'
    p.idx_extension = 'index'
    idx = index.Index('rtree_index', properties=p)
    n_components = 70
    encodings = []
    pca = PCA(n_components=n_components, whiten=True)
    i = 0
    for img in listdir('fotos_bd/'):
        print(i)
        i += 1
        encodings.append(encode_file(f'fotos_bd/{img}'))
    i = 0
    encodings = pca.fit(encodings)
    for enc in encodings:
        idx.insert(i, tuple(enc))
    idx.close()