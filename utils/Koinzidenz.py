import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

def f (t,N,tau):
    return N*np.exp(-(t)/tau)
#read in files
path = "/home/piet/Dokumente/measurements/org_conc_spec/10m/"

data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",", filling_values="0.")
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
Decay = mu_Decay[:, 1]
capture = mu_capture[:, 1]
nonPrimaries = mu_nonPrimaries[:, 1]
primaries = mu_primaries[:, 1]

mu_capture_Sc1 = mu_capture[mu_capture[:, 7] < 1.1]
mu_capture_Sc2 = mu_capture[mu_capture[:, 7] > 1.1]

high_capture = capture[capture > 1.]

print "Capture: " + str(np.shape(capture))
print "Decay: " + str(np.shape(Decay))
print "Primaries: " + str(np.shape(primaries))
print "nonPrimaries: " + str(np.shape(nonPrimaries))
#plt.hist(nonPrimaries, 100, histtype='step' , color="green")
#plt.hist(primaries, 10, histtype='step', color="blue")
#n, bins, patches = plt.hist(mu_capture_Sc1[:, 1], bins=np.linspace(0, 10000, 101), color="red")
n2, bins2, patches2 = plt.hist(high_capture, bins=np.linspace(10., 18000., 101), color="blue")
bin_mids = -(bins2[1]-bins2[0])/2.+bins2[1:]
print capture
print "Momente"
capture_Sc1 = mu_capture_Sc1[:, 1]
capture_Sc2 = mu_capture_Sc2[:, 1]


print np.mean(capture_Sc1[capture_Sc1 < 0.3])-0.08
print np.mean(capture_Sc2[capture_Sc2 < 1.])-0.47
print "fern:"
print np.mean(capture[capture > 1.])
print len(primaries) + len(nonPrimaries) + len(Decay)


#plt.plot(bin_mids, n)
plt.title("Capture Events over time (10M primaries)")
plt.xlabel("$t$ in $[ns]$")
plt.ylabel("# of Capture events")
popt, pcov = curve_fit(f, bin_mids, n2, bounds=([0., 0.], [300000.,  30000.]))
print popt
#sciGrieder Cosmic Rays at Earth
# plt.plot(n2, f(bin_mids, *popt))
#plt.hist(nonPrimaries, 100, histtype='step', color='blue')
#plt.hist(primaries, 100, color='green')
plt.show()
