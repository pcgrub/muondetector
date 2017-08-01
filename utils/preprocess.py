import numpy as np

path = "/home/piet/Dokumente/build42-testmuon/"

data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
m = np.concatenate((data0, data1, data2, data3))

mu_rel = m[m[:, 4] > 0.9]
mu_Decay = mu_rel[mu_rel[:, 4] == 1.]
mu_capture = mu_rel[mu_rel[:, 4] == 2.]
mu_BoundDecay = mu_rel[mu_rel[:, 4] == 3.]
mu_Ioni = mu_rel[mu_rel[:, 4] == 4.]
mu_nonDecay = m[m[:, 4] < 0.1]
#mu_primaries = mu_nonDecay[((mu_nonDecay[:, 5] == 3.) or (mu_nonDecay[:, 5] == 4.))]
mu_nonPrimaries = mu_nonDecay[(mu_nonDecay[:, 5] < 3.)]
mu_protons = mu_nonDecay[(mu_nonDecay[:, 5] == 5.)]

mu_gamma = mu_nonPrimaries[mu_nonPrimaries[:, 5] < 0.1]
mu_other = mu_nonPrimaries[mu_nonPrimaries[:, 5] > 0.1]

#primaries_Sc2 = mu_primaries[mu_primaries[:, 7] > 1]

#print len(primaries_Sc2)
#print len(mu_other)
#print len(real_others)
#print rel_Decay[:, 0]
#print len(rel_Decay)
#print len(mu_Decay)
#print len(mu_primaries) - 2*len(primaries_Sc2)
#print mu_Decay[:, 0]
#print primaries_Sc2[:, 0]
#print np.mean(mu_Decay[:, 6])
#print np.mean(rel_Decay[:, 6])

np.savetxt(path+"decay.csv", mu_Decay, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"capture.csv", mu_capture, delimiter=",", fmt="%7.7f", newline="\n")
#np.savetxt(path+"primaries.csv", mu_primaries, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"protons.csv", mu_protons, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"gamma.csv", mu_gamma, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"other.csv", mu_other, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"bound.csv", mu_BoundDecay, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"ioni.csv", mu_Ioni, delimiter=",", fmt="%7.7f", newline="\n")

