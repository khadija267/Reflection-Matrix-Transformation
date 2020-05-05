
import numpy as np
from numpy.linalg import norm, inv
from numpy import transpose
#a bear drawing code Example to manipulte reflection
from fns import *
# caculating transformation matrix T,
# having it out of an orthonormal basis set E
# and a transformation matrix in the mirror's coordinates TE.
def build_reflection_matrix(basis) : # The parameter basis is a 2×2 matrix that is passed to the function.
    E = gsBasis(basis)
    TE = np.array([[1, 0],
                   [0, -1]])
    T = E@TE@inv(E)
    return T
##########################TEST####################3
# First load Pyplot, a graph plotting library.
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
#basis can be changed
bearBasis = np.array(
    [[1,   -1],
     [1.5, 2]])
T = build_reflection_matrix(bearBasis)
reflected_bear_white_fur = T @ bear_white_fur
reflected_bear_black_fur = T @ bear_black_fur
reflected_bear_face = T @ bear_face
#set up the graphics environment from fns.py file
ax = draw_mirror(bearBasis)
#plot the bear
ax.fill(bear_white_fur[0], bear_white_fur[1], color=bear_white, zorder=1)
ax.fill(bear_black_fur[0], bear_black_fur[1], color=bear_black, zorder=2)
ax.plot(bear_face[0], bear_face[1], color=bear_white, zorder=3)
#reflection plot
ax.fill(reflected_bear_white_fur[0], reflected_bear_white_fur[1], color=bear_white, zorder=1)
ax.fill(reflected_bear_black_fur[0], reflected_bear_black_fur[1], color=bear_black, zorder=2)
ax.plot(reflected_bear_face[0], reflected_bear_face[1], color=bear_white, zorder=3);
