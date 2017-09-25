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
meanflow = data[0:, 3] + data[0:, 4]
val = data[0:, 2]*1000.
E_kin1 = p_to_Ekin(val)
E_flow1 = E_kin1*meanflow/(val*1000.)
errors = data[:, 7]

E_errors = E_kin1*errors/(val*1000.)
lower_bins = p_to_Ekin(data[0:, 0]*1000.)
upper_bins = p_to_Ekin(data[0:, 1]*1000.)

area = (upper_bins-lower_bins)*E_flow1
print area.sum()
print type(E_errors)
print len(E_flow1)
er = (E_errors[3:])
#er = np.column_stack((E_errors[3:], E_errors[3:]))
#er = er.T()
print er
#print upper_limits
plt.errorbar(E_kin1[3:], E_flow1[3:], yerr=er, fmt='.', label="Messwerte von CAPRICE94")
plt.plot(E_kin1[:3], E_flow1[:3], 'r.', label="Extrapolation")
plt.plot()
plt.ylabel("$I_V$ $[(m^2 \; s \;GeV \; sr)^{-1}]$")
plt.xlabel("$E_{kin} [MeV]$")

#plt.plot(E_kin, -dN)
#plt.title("differentiell$")
plt.xscale("log")
plt.yscale("log")
plt.xlim((1, 1000000))
plt.legend(loc=3)
plt.show()
