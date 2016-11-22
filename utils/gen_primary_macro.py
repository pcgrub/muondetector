import numpy as np
from matplotlib import pyplot as plt

def write_angles(f, lower_limit,upper_limits, angles):
    # set histogram defined user interaction for the angular distribution
    f.write("/gps/ang/type user\n")
    # write initial lower limit
    f.write("/gps/hist/type theta\n")

    f.write("/gps/hist/point " + str(lower_limit) + " 0.\n")
    for i, val in enumerate(angles):
        f.write("/gps/hist/point " + str(upper_limits[i]) + " " + str(val) + "\n")
    f.write("/gps/hist/type phi\n")
    f.write("/gps/hist/point 0. 0.\n")
    f.write("/gps/hist/point 6.282 4.\n")

def write_energies(f, lower_limit,upper_limits, energies):
    f.write("/gps/ene/type Arb\n")
    f.write("/gps/ene/diffspec 0\n")
    f.write("/gps/hist/type arb\n")
    f.write("/gps/hist/point " + str(lower_limit) + " 0.\n")
    for i, val in enumerate(energies):
        f.write("/gps/hist/point " + str(upper_limits[i]) + " " + str(val) + "\n")
    f.write("/gps/hist/inter Lin\n")

def write_to_text(path,low_an,ang_upper_limits, angles, low_e, e_upper_lims, energies):
    # open file to write to
    f = open(path + "primary_conc.mac", "w")

    # set energy
    # histogram defined energy will be added later
    #f.write("/gps/position 0. 0. -170. cm\n")
    f.write("/gps/pos/type Plane\n")
    f.write("/gps/pos/shape Square\n")
    f.write("/gps/pos/centre 0. 0. -1. cm\n")
    f.write("/gps/pos/halfx 0.25 m\n")
    f.write("/gps/pos/halfy 0.15 m\n")
    write_energies(f, low_e, e_upper_lims, energies)
    write_angles(f, low_an, ang_upper_limits, angles)
    f.close()


# get energies from calibration file
data = np.genfromtxt("energy_calibration/conc_energy_cali.csv", delimiter=",")
muon_mass_MeV = 105.65837
ang_data = np.genfromtxt("energy_calibration/angular_cali.csv", delimiter=",")
path = "/home/piet/Dokumente/muondetector/"

#change momentum to energie
#for i in range(3):
#    data[:, i] = np.sqrt(muon_mass_MeV**2 + (1000*data[:, i])**2)

#energies
print data
lowest_bin = data[0, 0]
e_upper_limits = data[:, 1]
#meanflow = data[:, 3] + data[:, 4]
meanflow = data[:, 3]
#angles

ang_lowest_bin = ang_data[0, 0]
ang_upper_limits = ang_data[:, 1]
values = ang_data[:, 3]

# set a 70 deg limit
#limit = .5*np.pi - np.deg2rad(20.)
#bins = np.linspace(0, limit, 37)
#ang_upper_limits = bins[1:]
#bin_size = (bins[1]-bins[0])/2.
#angles = ang_upper_limits-bin_size
#values = (np.cos(angles))**2

# write to text file primary.mac
write_to_text(path, ang_lowest_bin, ang_upper_limits, values, lowest_bin, e_upper_limits, meanflow)
plt.xscale('log')
plt.yscale('log')
plt.plot(data[:, 2], meanflow)
#plt.plot(angles, values)
#plt.show()
