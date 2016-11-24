import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Levy distribution function
def f(t, m, c):
    return np.sqrt(c/(2.*np.pi*(t-m)**3.))*np.exp(-c/(2.*(t-m)))

# approximation landau
def g(t, A):
    return A*np.exp(-0.5*(t+np.exp(-t)))



data = np.genfromtxt("energy_calibration/energy_cali_E.csv", delimiter=",")

lowest_bins = data[0:0]
upper_limits = data[:, 1]
meanflow = data[:, 3] + data[:, 4]
plt.xscale('log')
plt.yscale('log')
plt.plot(data[:, 2], meanflow)
popt, pcov = curve_fit(f, data[:, 2], meanflow, bounds=([0., 0.], [0.00000001, 10.]))
print popt
#plt.plot(data[:, 2], f(data[:, 2], *popt))
plt.show()
