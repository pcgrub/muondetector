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
    np.savetxt(path, output, delimiter=",", fmt="%7.5f", newline="\n")


#path2 = "/home/piet/Dokumente/measurements/test/from_measurement/"
#path2 = "/home/piet/Dokumente/source-cali/"
path = "/home/piet/Dokumente/measurements/cali_conc/10m_normale/"

# read in data
data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
muon = np.concatenate((data0[data0[:, 5] > 2.], data1[data1[:, 5] > 2.], data2[data2[:, 5] > 2.],
                       data3[data3[:, 5] > 2.]))
"""
data4 = np.genfromtxt(path2+"muon_Hits_nt_data_t0.csv", delimiter=",")
data5 = np.genfromtxt(path2+"muon_Hits_nt_data_t1.csv", delimiter=",")
data6 = np.genfromtxt(path2+"muon_Hits_nt_data_t2.csv", delimiter=",")
data7 = np.genfromtxt(path2+"muon_Hits_nt_data_t3.csv", delimiter=",")
muon2 = np.concatenate((data4[data4[:, 5] > 2.], data5[data5[:, 5] > 2.], data6[data6[:, 5] > 2.],
                       data7[data7[:, 5] > 2.]))
"""

#print muon
#calculate theta from momentum's z-component
#z = muon[:, 8]
#theta = np.arccos(z)
#z2 = muon2[:, 8]
#theta2 = np.arccos(z2)
#print z

#extract energy
E = muon[:, 3]
#E2 = muon2[:, 3]
#print E

#initialize plotting window
fig = plt.figure()
#ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(111)

#plotting angular distribution
#n, bins, patches = ax1.hist(theta, 100, histtype="step")
#ax1.hist(theta2, bins=bins, histtype="step")
#ax1.set_title("Angular Distribution of N=" + str(len(theta)) + " events")
#ax1.set_xlabel("angle [rad]")
#ax1.set_ylabel("# of events")

# fitting the bin_mids and heights of the histogram
#bin_mids = -(bins[1]-bins[0])/2.+bins[1:]
#popt, pcov = curve_fit(f, bin_mids, n, bounds=(0., 300000.))
#print popt
#ax1.plot(bin_mids, f(bin_mids, *popt))

#plotting energy distribution
n_2, bins_2, patches_2 = ax2.hist(E, bins=np.logspace(-1.0, 6., 101),
                                  histtype="step", label="concrete")
#ax2.hist(E2, bins=bins_2, histtype="step", label="air")
ax2.set_title("Energy Distribution WITH low energy extrapolation" + str(len(E)) + " events")
ax2.set_xlabel("Energy [MeV]")
ax2.set_ylabel("# of events")
ax2.set_xscale('log')
ax2.set_yscale('log')

#print E2
#print min(E2)
#print max(E2)

print max(E)

energy_file_path = "/home/piet/Dokumente/muondetector/utils/energy_calibration/conc_energy_cali_without_low.csv"
anular_file_path = "/home/piet/Dokumente/muondetector/utils/energy_calibration/angular_cali_without_low.csv"
#write_hist_file(bins, n, anular_file_path)
#write_hist_file(bins_2, n_2, energy_file_path)

# fitting bin mids and such:
plt.legend()
plt.show()
