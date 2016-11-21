import numpy as np

data = np.genfromtxt("energy_cali.csv", delimiter=",")
muon_mass_MeV = 105.65837

#change momentum to energie
for i in range(3):
    data[:, i] = np.sqrt(muon_mass_MeV**2 + (1000*data[:, i])**2)

np.savetxt("energy_cali_E.csv", data, delimiter=",", fmt="%7.7f", newline="\n")