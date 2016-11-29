import numpy as np
from matplotlib import pyplot as plt

def p_to_Ekin(p):
    m = 105.65837
    return np.sqrt(p**2+m**2)-m

def Ekin_to_p(E_ges):
    m = 105.65837
    E = E_ges - m
    return np.sqrt(E*(E+2*m))


muon_mass_MeV = 105.65837

#print dN
#print E_kin
data = np.genfromtxt("energy_calibration/energy_cali.csv", delimiter=",")


#lowest_bins = Ekin_to_p(data[0:0])
#upper_limits = Ekin_to_p(data[:, 1])
meanflow = data[3:, 3] + data[3:, 4]
val = data[3:, 2]*1000.
E_kin1 = p_to_Ekin(val)
E_flow1 = E_kin1*meanflow/val

lower_bins = p_to_Ekin(data[3:, 0]*1000.)
upper_bins = p_to_Ekin(data[3:, 1]*1000.)

area = (upper_bins-lower_bins)*E_flow1
print area.sum()
#print upper_limits
plt.plot(E_kin1, E_flow1, 'b.', label="Experimental Data")
plt.ylabel("Intensity $[(m^2sGeV)^{-1}]$")
plt.xlabel("$E_{kin} [MeV]$")

#plt.plot(E_kin, -dN)
plt.title("differential energy spectrum $\mu+/\mu-$")
plt.xscale("log")
plt.yscale("log")
plt.xlim((1, 1000000))
plt.legend()
plt.show()
