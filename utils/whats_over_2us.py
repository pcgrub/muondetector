from matplotlib import pyplot as plt
import numpy as np
import time as t

def sc1sc2(mat, column=7):
    """seperates input array for copper, scint1 and scint2 for volume in
    which detected for column=7 or origin volume column=6"""
    if (column==6):
        return  mat[mat[:, column] == 1], mat[mat[:, column] == 3], mat[mat[:, column] == 2]
    return  mat[mat[:, column] == 1], mat[mat[:, column] == 2], mat[mat[:, column] == 3]

def timecolumn(mat):
    return mat[:,1]
path = "/Users/piet/Documents/build-muondetector/"
bound = np.genfromtxt(path+"bounddecayelectrons.csv", delimiter=",")
decay = np.genfromtxt(path+"decayelectrons.csv", delimiter=",")

bound_SC = sc1sc2(bound)[:2]
decay_SC = sc1sc2(decay)[:2]

bound_time = np.empty(2, dtype=np.ndarray)
bound_time[0] = timecolumn(bound_SC[0])
bound_time[1] = timecolumn(bound_SC[1])

decay_time = np.empty(2, dtype=np.ndarray)
decay_time[0] = timecolumn(decay_SC[0])
decay_time[1] = timecolumn(decay_SC[1])

bound_time[0] = bound_time[0][bound_time[0] > 2000.]
bound_time[1] = bound_time[1][bound_time[1] > 2000.]
decay_time[0] = decay_time[0][decay_time[0] > 2000.]
decay_time[1] = decay_time[1][decay_time[1] > 2000.]

print len(bound_time[0])
print len(bound_time[1])
print len(decay_time[0])
print len(decay_time[1])

fig = plt.figure()

SC1 = bound_time[0], decay_time[0]
SC2 = bound_time[1], decay_time[1]

ax1 = fig.add_subplot(121)
ax1.hist(SC1, 100, stacked=True)

ax2 = fig.add_subplot(122)
ax2.hist(SC2, 100, stacked=True)
plt.show()

