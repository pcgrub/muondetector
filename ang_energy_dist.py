import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# fit function for the angular distribution:
def f(x, A):
    return A*np.cos(x)**2

def write_hist_file(bins, n, path):
    bin_size = (bins[1]-bins[0])
    bin_mid = bins[1:] - 0.5*bin_size
    output = np.column_stack((bins[:-1], bins[1:], bin_mid, n))
    np.savetxt(path, output, delimiter=",", fmt="%7.7f", newline="\n")


path = "/home/piet/Dokumente/measurements/atmo/1m/"

# read in data
data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
muon = np.concatenate((data0[data0[:, 5] > 2.], data1[data1[:, 5] > 2.], data2[data2[:, 5] > 2.],
                       data3[data3[:, 5] > 2.]))

print muon
#calculate theta from momentum's z-component
z = muon[:, 8]
theta = np.arccos(-z)
#print z

#extract energy
E = muon[:, 3]
print E

#initialize plotting window
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#plotting angular distribution
n, bins, patches = ax1.hist(theta, 100)
ax1.set_title("Angular Distribution of N=" + str(len(theta)) + " events")
ax1.set_xlabel("angle [rad]")
ax1.set_ylabel("# of events")

# fitting the bin_mids and heights of the histogram
bin_mids = -(bins[1]-bins[0])/2.+bins[1:]
popt, pcov = curve_fit(f, bin_mids, n, bounds=(0., 300000.))
print popt
ax1.plot(bin_mids, f(bin_mids, *popt))

#plotting energy distribution
n_2, bins_2, patches_2 = ax2.hist(E, bins=np.logspace(2.0, 5.08, 101))
ax2.set_title("Energy Distribution of N=" + str(len(E)) + " events")
ax2.set_xlabel("Energy [MeV]")
ax2.set_ylabel("# of events")
ax2.set_xscale('log')
ax2.set_yscale('log')

energy_file_path = "/home/piet/Dokumente/myon-detector/utils/energy_calibration/conc_energy_cali.csv"
anular_file_path = "/home/piet/Dokumente/myon-detector/utils/energy_calibration/angular_cali.csv"
write_hist_file(bins, n, anular_file_path)
write_hist_file(bins_2, n_2, energy_file_path)

# fitting bin mids and such:
plt.show()
