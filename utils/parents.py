import matplotlib.pyplot as plt
import numpy as np

path="/Users/piet/Documents/build-muondetector/"
bound = np.genfromtxt(path+"capturedelectrons.csv", delimiter=",")

secondary = bound[bound[:,10] == 1]
non_secondary = bound[bound[:,10] != 1]

print "Bound Decay mit Muon als Parent"
print len(secondary)

print "andere"
print len(non_secondary)
