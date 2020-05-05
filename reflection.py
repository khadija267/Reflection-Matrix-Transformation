
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

# This is the matrix of Bear's basis vectors.
# (When you've done the exercise once, see what happns when you change Bear's basis.)
bearBasis = np.array(
    [[1,   -1],
     [1.5, 2]])
# This line uses your code to build a transformation matrix for us to use.
T = build_reflection_matrix(bearBasis)

# Bear is drawn as a set of polygons, the vertices of which are placed as a matrix list of column vectors.
# We have three of these non-square matrix lists: bear_white_fur, bear_black_fur, and bear_face.
# We'll make new lists of vertices by applying the T matrix you've calculated.
reflected_bear_white_fur = T @ bear_white_fur
reflected_bear_black_fur = T @ bear_black_fur
reflected_bear_face = T @ bear_face

# This next line runs a code to set up the graphics environment.
ax = draw_mirror(bearBasis)

# We'll first plot Bear, his white fur, his black fur, and his face.
ax.fill(bear_white_fur[0], bear_white_fur[1], color=bear_white, zorder=1)
ax.fill(bear_black_fur[0], bear_black_fur[1], color=bear_black, zorder=2)
ax.plot(bear_face[0], bear_face[1], color=bear_white, zorder=3)

# Next we'll plot Bear's reflection.
ax.fill(reflected_bear_white_fur[0], reflected_bear_white_fur[1], color=bear_white, zorder=1)
ax.fill(reflected_bear_black_fur[0], reflected_bear_black_fur[1], color=bear_black, zorder=2)
ax.plot(reflected_bear_face[0], reflected_bear_face[1], color=bear_white, zorder=3);
    
