import numpy as np

path = "/home/piet/Dokumente/measurements/Koinzidenz/10m/"

data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
m = np.concatenate((data0, data1, data2, data3))

mu_rel = m[m[:, 4] > 0.9]
mu_Decay = mu_rel[mu_rel[:, 4] < 1.1]
mu_capture = mu_rel[mu_rel[:, 4] > 1.9]
mu_nonDecay = m[m[:, 4] < 0.1]

mu_primaries = mu_nonDecay[(mu_nonDecay[:, 5] >= 3.)]
mu_nonPrimaries = mu_nonDecay[(mu_nonDecay[:, 5] < 3.)]

mu_gamma = mu_nonPrimaries[mu_nonPrimaries[:, 5] < 0.1]
mu_other = mu_nonPrimaries[mu_nonPrimaries[:, 5] > 0.1]

primaries_Sc2 = mu_primaries[mu_primaries[:, 7] > 1]
truth = np.in1d(np.round(mu_other[:, 0]), np.round(primaries_Sc2[:, 0]), invert=True)
truth2 = np.in1d(np.round(mu_gamma[:, 0]), np.round(primaries_Sc2[:, 0]), invert=True)
truth3 = np.in1d(np.round(mu_capture[:, 0]), np.round(primaries_Sc2[:, 0]), invert=True)
truth4 = np.in1d(np.round(mu_Decay[:, 0]), np.round(primaries_Sc2[:, 0]), invert=True)
real_others = mu_other[truth]
rel_gamma = mu_gamma[truth2]
rel_capture = mu_capture[truth3]
rel_Decay = mu_Decay[truth4]

print len(primaries_Sc2)
print len(mu_other)
print len(real_others)
print rel_Decay[:, 0]
print len(rel_Decay)
print len(mu_Decay)
print len(mu_primaries) - 2*len(primaries_Sc2)
print mu_Decay[:, 0]
print primaries_Sc2[:, 0]
print np.mean(mu_Decay[:, 6])
print np.mean(rel_Decay[:, 6])

np.savetxt(path+"decay.csv", mu_Decay, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"capture.csv", mu_capture, delimiter=",", fmt="%7.7f", newline="\n")
#np.savetxt(path+"primaries.csv", mu_primaries, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"gamma.csv", mu_gamma, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"other.csv", mu_other, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"rel_other.csv", real_others, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"rel_gamma.csv", rel_gamma, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"rel_capture.csv", rel_capture, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"rel_decay.csv", rel_Decay, delimiter=",", fmt="%7.7f", newline="\n")
