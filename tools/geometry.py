import numpy as np

translation = np.array([
    [ 0. ,  0. ,  0. ],
    [ 0.2,  0.2,  0. ],
    [ 2. ,  1.5, -0.5],
    [ 1.2, -0.5,  0.5],
    [-0.5, -0.5, -0.5]])

_irt2 = 1./np.sqrt(2.)
direction = np.array([
    [   1. ,    0. ,    0. ],
    [   0. ,    1. ,    0. ],
    [   0. ,    0. ,    1. ],
    [  -1. ,    0. ,    0. ],
    [   0. ,   -1. ,    0. ],
    [   0. ,    0. ,   -1. ],
    [ _irt2,  _irt2,    0. ],
    [   0. ,  _irt2,  _irt2],
    [ _irt2,    0. ,  _irt2],
    [-_irt2,  _irt2,    0. ],
    [   0. , -_irt2,  _irt2],
    [-_irt2,    0. ,  _irt2],
    [ _irt2, -_irt2,    0. ],
    [   0. ,  _irt2, -_irt2],
    [ _irt2,    0. , -_irt2],
    [-_irt2, -_irt2,    0. ],
    [   0. , -_irt2, -_irt2],
    [-_irt2,    0. , -_irt2]
])