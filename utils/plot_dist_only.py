import numpy as np
from matplotlib import pyplot as plt

path = "/home/piet/Dokumente/build-muondetector/"

# read in data
data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
print data0
muon = np.concatenate((data0, data1, data2, data3))

E = muon[:, 3]
print E.min()
print E.max()
plt.hist(E, bins=np.logspace(1.0, 5.08, 101))
plt.xscale("log")
plt.yscale("log")
plt.show()
