from matplotlib import pyplot as plt
import numpy as np

path = "/home/piet/Dokumente/measurements/org_conc_spec/10m/"

# read in all the arrays from the csv
data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
mu_10k = np.concatenate((data0, data1, data2, data3))

# Decay flags are in column 5(4)
# get data of decayed particles only in the second scintillator
#log =np.logical_and(muplus_10k[:, 9] < 0.1 , muplus_10k[:, 10] < 3)

#relevant groups

#first split into relevant and non Decay
mu_rel = mu_10k[mu_10k[:, 4] > 0.9]
mu_nonDecay = mu_10k[(mu_10k[:, 4] < 0.1)]

# split relevant in Decay and Capture
mu_Decay = mu_rel[mu_rel[:, 4] < 1.1]
mu_capture = mu_rel[mu_rel[:, 4] > 1.1]

# split other into primaries and secondaries
mu_primaries = mu_nonDecay[mu_nonDecay[:, 5] > 2.1]
mu_nonPrimaries = mu_nonDecay[mu_nonDecay[:, 5] < 2.1]

# and the non primaries in gamma and electrons/positrons
mu_gamma = mu_nonPrimaries[mu_nonPrimaries[:, 5] < 0.1]
mu_other = mu_nonPrimaries[mu_nonPrimaries[:, 5] > 0.1]

print "quantities:"
print "Primaries: " + str(len(mu_primaries))
print "Decay: " + str(len(mu_Decay))
print "Capture: " + str(len(mu_capture))
print "Gamma: " + str(len(mu_gamma))
print "Other: " + str(len(mu_other))

plt.title("10m primary particles simulation ")
plt.xlabel("Time [ns]")
plt.ylabel("$\Delta E$ $[MeV]$")
plt.plot(mu_primaries[:, 1], mu_primaries[:, 2], 'c.', label="primaries", ms=3)
plt.plot(mu_other[:, 1], mu_other[:, 2], 'g.', label="other", ms=3)
plt.plot(mu_capture[:, 1], mu_capture[:, 2], 'b.', label="capture", ms=3)
plt.plot(mu_Decay[:, 1], mu_Decay[:, 2], 'r.', label="Decay", ms=3)
plt.plot(mu_gamma[:, 1], mu_gamma[:, 2], 'y.', label="gamma", ms=3)
plt.xscale("log")
#plt.yscale("log")
plt.legend()
plt.show()
