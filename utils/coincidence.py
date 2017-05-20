import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats


def f(t, N):
    tau = 2197
    return N*np.exp(-t/tau)


def f2(t, N,tau):
    return N*np.exp(-t/tau)

#read in files
path = "/mnt/Daten/Documents/Physik Bachelor/Bachelorarbeit/measurements/new/org_conc_spec/10m/"

decay = np.genfromtxt(path+"decay.csv", delimiter=",")
capture = np.genfromtxt(path+"capture.csv", delimiter=",")
#primaries = np.genfromtxt(path+"primaries.csv", delimiter=",")
other = np.genfromtxt(path+"rel_other.csv", delimiter=",")
#gamma = np.genfromtxt(path+"gamma.csv", delimiter=",")
#rel_others = np.genfromtxt(path+"rel_other.csv", delimiter=",")


#primaries_Sc1 = primaries[primaries[:, 7] < 1.1]
#primaries_Sc2 = primaries[primaries[:, 7] > 1.1]
capture_Sc1 = capture[capture[:, 7] < 1.1]
capture_Sc2 = capture[capture[:, 7] > 1.1]
decay_Sc1 = decay[decay[:, 7] < 1.1]
decay_Sc2 = decay[decay[:, 7] > 1.1]
other_Sc1 = other[other[:, 7] < 1.1]
other_Sc2 = other[other[:, 7] > 1.1]
#gamma_Sc1 = gamma[gamma[:, 7] < 1.1]
#gamma_Sc2 = gamma[gamma[:, 7] > 1.1]

high_capture_Sc1 = capture_Sc1[capture_Sc1[:, 1] > 10]
high_capture_Sc2 = capture_Sc2[capture_Sc2[:, 1] > 10]
low_capture_Sc1 = capture_Sc1[capture_Sc1[:, 1] < 10]
low_capture_Sc2 = capture_Sc2[capture_Sc2[:, 1] < 10]

high_capture = np.concatenate((high_capture_Sc1, high_capture_Sc2))
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(122)

#ax1.hist(low_capture_Sc1[:, 1], bins=np.linspace(0, 2, 101), histtype="step", label="$\mu^-$-Einfang")
#ax2.hist(low_capture_Sc2[:, 1], bins=np.linspace(0, 2, 101), histtype="step", label="$\mu^-$-Einfang")


#plt.hist(nonPrimaries, 100, histtype='step' , color="green")
#plt.hist(primaries, 10, histtype='step', color="blue")
bin_lims = np.linspace(0, 2000, 30)

n, bins, patches = ax1.hist((decay[:, 1], high_capture[:, 1]), bins=bin_lims, color=["green", "blue"],label=["Zerfall","$\mu^-$-Einfang"] ,stacked=True, histtype="bar")
#n2, bins2, patches2 = ax2.hist((decay_Sc2[:, 1], high_capture_Sc2[:, 1]), bins=bin_lims, color=["green", "blue"], stacked=True, histtype="bar")

#plt.plot(bin_mids, n)

ax1.set_title("Zeitverhalten von Zerfall und Einfang in der Simulation")
#ax2.set_title("SC2")
ax1.set_xlabel("$t$ in $[ns]$")
#ax2.set_xlabel("$t$ in $[ns]$")
ax1.set_ylabel("Anzahl Events")

#ax1.set_yscale("log")
#ax2.set_yscale("log")

#plt.ylim((1, 900))

bin_mids = bins[:-1] + 0.5*(bins[1]-bins[0])
popt, pcov = curve_fit(f, bin_mids, n[0], bounds=(0., 300000.))
#popt2, pcov2 = curve_fit(f, bin_mids, n2[0], bounds=(0., 300000.))
popt3, pcov3 = curve_fit(f2, bin_mids, n[1], bounds=([0., 1843.], [30000000., 1843.5]))
#popt4, pcov4 = curve_fit(f2, bin_mids, n2[1], bounds=([0., 1869.], [30000000., 1870]))
#print popt3
#print np.sqrt(np.diag(pcov3))/np.sqrt(popt3)
#print popt4
#print np.sqrt(np.diag(pcov4))/np.sqrt(popt4)
print
print "all"
print np.mean(capture_Sc1[:, 1])
print np.std(capture_Sc1[:, 1])/np.sqrt(len(capture_Sc1[:, 1]))
print np.mean(capture_Sc2[:, 1])
print np.std(capture_Sc2[:, 1])/np.sqrt(len(capture_Sc2[:, 1]))
print "low"
print np.mean(high_capture_Sc1[:, 1])
print np.std(high_capture_Sc1[:, 1])/np.sqrt(len(high_capture_Sc1[:, 1]))
print np.mean(high_capture_Sc2[:, 1])
print np.std(high_capture_Sc2[:, 1])/np.sqrt(len(high_capture_Sc2[:, 1]))


ax1.plot(bin_mids, f(bin_mids, popt), '-r')
#ax2.plot(bin_mids, f(bin_mids, popt2), '-r', label='Zerfall')
ax1.plot(bin_mids, f2(bin_mids, *popt3), 'r-')
#ax2.plot(bin_mids, f2(bin_mids, *popt4), 'r-', label='$\mu^-$-Einfang')
#plt.plot(bin_mids, f(bin_mids, *popt2))
print popt3+popt
ax1.legend()
#ax2.legend()
plt.show()
