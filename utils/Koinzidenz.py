import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def f (t,N,tau):
    return N*np.exp(-(t)/tau)
#read in files
mu_1m = np.genfromtxt('mu_1m.csv', delimiter=',')


mu_Decay = mu_1m[mu_1m[:, 4] > 0.9]
mu_nonDecay = mu_1m[(mu_1m[:, 4] < 0.1)]
mu_primaries = mu_nonDecay[(mu_nonDecay[:, 5] >= 3.)]
mu_nonPrimaries = mu_nonDecay[(mu_nonDecay[:, 5] < 3.)]
Decay = mu_Decay[:,1]
nonPrimaries = mu_nonPrimaries[:, 1]
primaries = mu_primaries[:,1]



print np.shape(Decay)
#plt.hist(nonPrimaries, 100, histtype='step' , color="green")
#plt.hist(primaries, 10, histtype='step', color="blue")
n, bins, patches = plt.hist(Decay, 100, color="red")
bin_mids = -(bins[1]-bins[0])/2.+bins[1:]

diff =np.median(primaries)

print np.median(nonPrimaries)
print np.median(Decay)
print np.mean(nonPrimaries)
print np.mean(Decay)
#print len(primaries) + len(nonPrimaries) + len(Decay)


plt.plot(bin_mids, n)
plt.title("Decay Events over time (1M primaries)")
plt.xlabel("$t$ in $[ns]$")
plt.ylabel("# of Decay events")
popt, pcov = curve_fit(f, bin_mids, n, bounds=(0., [300000.,  30000.]))
print popt
plt.plot(bin_mids, f(bin_mids, *popt))
#plt.hist(nonDecay_nonprim, 100, histtype='step', color='blue')
#plt.hist(primaries, 100, color='green')
plt.show()
