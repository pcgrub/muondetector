from matplotlib import pyplot as plt
import numpy as np

# read in all the arrays from the csv
mu_10k = np.genfromtxt('mu_10k.csv', delimiter=',')

# Decay flags are in column 5(4)
# get data of decayed particles only in the second scintillator
#log =np.logical_and(muplus_10k[:, 9] < 0.1 , muplus_10k[:, 10] < 3)

#mu+
#scintillator 1 split decay and non decay
mu_Decay = mu_10k[mu_10k[:, 4] > 0.9]
mu_nonDecay = mu_10k[(mu_10k[:, 4] < 0.1)]

#decay
muplus_Decay = mu_Decay[mu_Decay[:, 5] == 3.]
muminus_Decay = mu_Decay[mu_Decay[:, 5] == 4.]

Decay_SC1 = mu_Decay[mu_Decay[:, 7] == 1.]
Decay_SC2 = mu_Decay[mu_Decay[:, 7] == 2.]

#nondecay
muplus_nonDecay = mu_nonDecay[mu_nonDecay[:, 5] == 3.]
muminus_nonDecay = mu_nonDecay[mu_nonDecay[:, 5] == 4.]

nonDecay_SC1 = mu_nonDecay[mu_nonDecay[:, 7] == 1.]
nonDecay_SC2 = mu_nonDecay[mu_nonDecay[:, 7] == 2.]

print len(muplus_Decay) + len(muplus_nonDecay)
print len(muminus_Decay) + len(muminus_nonDecay)

plt.title(r"$\mu+$ and $\mu-$  at $20MeV$ in SC1 and SC2 ($10k$ primary particles)")
plt.xlabel("$E_{kin}$ at Origin $[MeV]$")
plt.ylabel("$\Delta E$ $[MeV]$")
plt.plot(Decay_SC2[:,3], Decay_SC2[:,2], 'r.', label="Decay")
plt.plot(nonDecay_SC2[:,3], nonDecay_SC2[:, 2], 'b.', label="other")
plt.plot(Decay_SC1[:,3], Decay_SC1[:,2], 'r.')#, label="Decay")
plt.plot(nonDecay_SC1[:,3], nonDecay_SC1[:, 2], 'b.')#, label="other")

plt.legend()
plt.show()
