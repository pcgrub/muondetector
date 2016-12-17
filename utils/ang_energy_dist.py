import numpy as np
from matplotlib import pyplot as plt
#import seaborn as sns
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
path = "/home/piet/Dokumente/measurements/absorption/10m_with_low/"
path2 = "/home/piet/Dokumente/measurements/absorption/10m_without_low/"
#path3 = "/home/piet/Dokumente/measurements/cali_conc/without_concrete/10m_without_low/"
#path4 = "/home/piet/Dokumente/measurements/cali_conc/10m_normale/"

# read in data
data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
#muon = np.concatenate((data0[data0[:, 5] > 2.], data1[data1[:, 5] > 2.], data2[data2[:, 5] > 2.],
#                       data3[data3[:, 5] > 2.]))
muon = np.concatenate((data0, data1, data2, data3))

data4 = np.genfromtxt(path2+"muon_Hits_nt_data_t0.csv", delimiter=",")
data5 = np.genfromtxt(path2+"muon_Hits_nt_data_t1.csv", delimiter=",")
data6 = np.genfromtxt(path2+"muon_Hits_nt_data_t2.csv", delimiter=",")
data7 = np.genfromtxt(path2+"muon_Hits_nt_data_t3.csv", delimiter=",")
#muon2 = np.concatenate((data4[data4[:, 5] > 2.], data5[data5[:, 5] > 2.], data6[data6[:, 5] > 2.],
#                       data7[data7[:, 5] > 2.]))
muon2 = np.concatenate((data4, data5, data6, data7))
"""
data8 = np.genfromtxt(path3+"muon_Hits_nt_data_t0.csv", delimiter=",")
data9 = np.genfromtxt(path3+"muon_Hits_nt_data_t1.csv", delimiter=",")
data10 = np.genfromtxt(path3+"muon_Hits_nt_data_t2.csv", delimiter=",")
data11 = np.genfromtxt(path3+"muon_Hits_nt_data_t3.csv", delimiter=",")
muon3 = np.concatenate((data8[data8[:, 5] > 2.], data9[data9[:, 5] > 2.], data10[data10[:, 5] > 2.],
                       data11[data11[:, 5] > 2.]))

data12 = np.genfromtxt(path4+"muon_Hits_nt_data_t0.csv", delimiter=",")
data13 = np.genfromtxt(path4+"muon_Hits_nt_data_t1.csv", delimiter=",")
data14 = np.genfromtxt(path4+"muon_Hits_nt_data_t2.csv", delimiter=",")
data15 = np.genfromtxt(path4+"muon_Hits_nt_data_t3.csv", delimiter=",")
muon4 = np.concatenate((data12[data12[:, 5] > 2.], data13[data13[:, 5] > 2.], data14[data14[:, 5] > 2.],
                       data15[data15[:, 5] > 2.]))

"""
#print muon
#calculate theta from momentum's z-component
#z = muon[:, 8]
#theta = np.arccos(z)
#z2 = muon2[:, 8]
#theta2 = np.arccos(z2)
#print z

abs = muon[muon[:, 3] > 0.9]
abs2 = muon2[muon2[:, 3] > 0.9]
#extract energy
E = abs[:, 2]
E2 = abs2[:, 2]
#E3 = muon3[:, 3]
#E4 = muon4[:, 3]
#print E

print E
print E2
#initialize plotting window
fig = plt.figure()
#fig.suptitle("Spektrumveraenderung der Myonen in Beton  $1.5m$ im Vergleich zu Luft")
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

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
ax1.hist(E, bins=np.logspace(-1.0, 6., 101), histtype="step", label="Absorption")
ax2.hist(E2, bins=np.logspace(-1.0, 6., 101), histtype="step", label="Absorption")
#ax2.hist(E3, bins=np.logspace(-1.0, 6., 101), histtype="step", label="Luft")
#ax2.hist(E4, bins=np.logspace(-1.0, 6., 101), histtype="step", label="Beton")

ax1.set_title("Mit Extrapolation")
ax1.set_xlabel("Energie [MeV]")
ax1.set_ylabel("Anzahl Hits")
ax1.set_xscale('log')
ax1.set_yscale('log')

#ax2.hist(E2, bins=bins_2, histtype="step", label="air")
ax2.set_title("Ohne Extrapolation")
ax2.set_xlabel("Energie [MeV]")
ax2.set_ylabel("Anzahl Hits")
ax2.set_xscale('log')
ax2.set_yscale('log')

#print E2
#print min(E2)
#print max(E2)

#print max(E)

#energy_file_path = "/home/piet/Dokumente/muondetector/utils/energy_calibration/conc_energy_cali_without_low.csv"
#nular_file_path = "/home/piet/Dokumente/muondetector/utils/energy_calibration/angular_cali_without_low.csv"
#write_hist_file(bins, n, anular_file_path)
#write_hist_file(bins_2, n_2, energy_file_path)

# fitting bin mids and such:
ax1.legend(loc=2)
ax2.legend(loc=2)
plt.show()
