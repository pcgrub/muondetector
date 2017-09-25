import numpy as np
from matplotlib import pyplot as plt

def p_to_Ekin(p):
    m = 105.65837
    return np.sqrt(p**2+m**2)-m

def Ekin_to_p(E_ges):
    m = 105.65837
    E = E_ges - m
    return np.sqrt(E*(E+2*m))

def p_to_E(p):
    m = 105.65837
    return np.sqrt(p ** 2 + m ** 2)

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

def write_energies_diff(f, lower_limit,upper_limits, energies):
    f.write("/gps/ene/type Arb\n")
    f.write("/gps/ene/diffspec 1\n")
    f.write("/gps/hist/type arb\n")
    f.write("/gps/hist/point " + str(lower_limit) + " 0.\n")
    for i, val in enumerate(energies):
        f.write("/gps/hist/point " + str(upper_limits[i]) + " " + str(val) + "\n")
    f.write("/gps/hist/inter Lin\n")

def write_energies_user(f, lower_limit,upper_limits, energies):
    f.write("/gps/ene/type User\n")
    f.write("/gps/hist/type energy\n")
    f.write("/gps/hist/point " + str(lower_limit) + " 0.\n")
    for i, val in enumerate(energies):
        f.write("/gps/hist/point " + str(upper_limits[i]) + " " + str(val) + "\n")

def write_to_text(path,low_an,ang_upper_limits, angles, low_e, e_upper_lims, energies, type):
    # open file to write to
    f = open(path, "w")

    # set energy
    # histogram defined energy will be added later
    #f.write("/gps/position 0. 0. -170. cm\n")
    f.write("/gps/pos/type Plane\n")
    f.write("/gps/pos/shape Square\n")
    f.write("/gps/pos/centre 0. 0. -1. cm\n")
    f.write("/gps/pos/halfx 0.25 m\n")
    f.write("/gps/pos/halfy 0.15 m\n")
    if type == "diff":
        write_energies_diff(f, low_e, e_upper_lims, energies)
    else:
        write_energies_user(f, low_e, e_upper_lims, energies)
    write_angles(f, low_an, ang_upper_limits, angles)
    f.close()

muon_mass_MeV = 105.65837
# get energies from calibration file
data = np.genfromtxt("energy_calibration/energy_cali.csv", delimiter=",")

# calibration file
ang_data = np.genfromtxt("energy_calibration/angular_cali.csv", delimiter=",")

# path for the macro file for atmospheric muons
path1 = "/home/piet/Dokumente/muondetector/primary_atmo.mac"

# energies for atmospheric muons form momentum spectrum in GeV
lowest_bin = p_to_Ekin(data[0, 0]*1000)
e_upper_limits = p_to_Ekin(data[:, 1]*1000)
mids = data[:, 2]*1000
total_flow = data[:, 3] + data[:, 4]
meanflow = p_to_E(mids)*(total_flow)/mids

# angles in cos^2 manner with 70 deg limit
limit = .5*np.pi - np.deg2rad(20.)
bins = np.linspace(0, limit, 37)
ang_upper_limits = bins[1:]
bin_size = (bins[1]-bins[0])/2.
angles = ang_upper_limits-bin_size
values = (np.cos(angles))**2

# write to text file primary_atmo.mac
write_to_text(path1, 0., ang_upper_limits, values, lowest_bin, e_upper_limits, meanflow, "diff")

# calibration file
conc_data = np.genfromtxt("energy_calibration/conc_energy_cali_without_low.csv", delimiter=",")

# path for the macro file for atmospheric muons that went through concrete
path2 = "/home/piet/Dokumente/muondetector/primary_conc.mac"

#energies from file (kinetic)
lowest_bin_conc = conc_data[0, 0]
e_upper_limits_conc = conc_data[:, 1]
mids_conc = conc_data[:, 2]
flow_conc = conc_data[:, 3]

#angles
ang_lowest_bin_conc = ang_data[0, 0]
ang_upper_limits_conc = ang_data[:, 1]
values_conc = ang_data[:, 3]


# write to text file primary_conc.mac
write_to_text(path2, ang_lowest_bin_conc, ang_upper_limits_conc, values_conc, lowest_bin_conc, e_upper_limits_conc,
              flow_conc, "user")

# optional plots for verfication purposes:
#plt.xscale('log')
#plt.yscale('log')
#plt.plot(p_to_Ekin(data[:, 2]*1000), meanflow)
#plt.plot(angles, values)
#plt.show()
