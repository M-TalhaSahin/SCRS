import pandas as pd
import os
import numpy as np
from scipy.sparse import csr_matrix
from numpy import savetxt


def get_sparse_matrix(dataFrameIn):
    N = len(dataFrameIn['OGRNO'].unique())
    M = len(dataFrameIn['DERS_KODU'].unique())

    # Map Ids to indices
    user_mapper = dict(zip(np.unique(dataFrameIn["OGRNO"]), list(range(N))))
    movie_mapper = dict(zip(np.unique(dataFrameIn["DERS_KODU"]), list(range(M))))

    # Map indices to IDs
    user_inv_mapper = dict(zip(list(range(N)), np.unique(dataFrameIn["OGRNO"])))
    movie_inv_mapper = dict(zip(list(range(M)), np.unique(dataFrameIn["DERS_KODU"])))

    user_index = [user_mapper[i] for i in dataFrameIn['OGRNO']]
    movie_index = [movie_mapper[i] for i in dataFrameIn['DERS_KODU']]

    X = csr_matrix((dataFrameIn["SAYISAL"], (movie_index, user_index)), shape=(M, N), dtype=np.float)

    return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper


os.chdir("..")
df = pd.read_excel('data/BrmOgrDers.xls', index_col=None, na_values=['NaN'], usecols="B, C, F, G", converters={'SAYISAL': float})

df = df[df.ORTALAMAYA_KAT != 0]
del df['ORTALAMAYA_KAT']


smx, userMap, movieMap, uinv_map, minv_map = get_sparse_matrix(df)
print(userMap.__len__())
print(movieMap.__len__())
print(movieMap.__len__()*userMap.__len__())

f = open('matrix.csv', 'w+')
smx.todense().tofile('matrix.csv')
savetxt('matrix.csv', smx.todense().data, delimiter=',')


