import numpy as np
from matplotlib import pyplot as plt

#read in files
mu_10k = np.genfromtxt('mu_10k.csv', delimiter=',')
mu_2MeV = np.genfromtxt('100keV.csv', delimiter=',')
mu_200MeV = np.genfromtxt('mu_200MeV_10k.csv', delimiter=',')

Decay_20MeV = mu_10k[mu_10k[:, 4] > 0.9]
Decay_2MeV = mu_2MeV[mu_2MeV[:, 4] > 0.9]
Decay_200MeV = mu_200MeV[mu_200MeV[:, 4] > 0.9]

print len(Decay_2MeV)
print len(Decay_20MeV)
print len(Decay_200MeV)


plt.title("Energy deposit (2MeV primaries)")
plt.xlabel("$\Delta E$ [MeV]")
plt.ylabel("# of Decays")
plt.hist(Decay_2MeV[:, 2], 50)
#plt.show()
