from matplotlib import pyplot as plt
import numpy as np

def sc1sc2(mat):
    """seperates input array for copper, scint1 and scint2"""
    return  mat[mat[:, 7] == 0], mat[mat[:, 7] == 1], mat[mat[:, 7] == 2]


#read in files
path = "/Users/piet/Desktop/testmitvakuumdetektoren/"

#path2 = "/home/piet/Dokumente/measurements/new/org_conc_spec/10k/"


decay = np.genfromtxt(path+"decayelectrons.csv", delimiter=",")
capture = np.genfromtxt(path+"capturedelectrons.csv", delimiter=",")
#primaries = np.genfromtxt(path+"muons.csv", delimiter=",")
other = np.genfromtxt(path+"otherelectrons.csv", delimiter=",")
gamma = np.genfromtxt(path+"gamma.csv", delimiter=",")
ioni = np.genfromtxt(path+"ionizationelectrons.csv", delimiter=",")
bound = np.genfromtxt(path+"bounddecayelectrons.csv", delimiter=",")
otherproton = np.genfromtxt(path+"otherprot.csv", delimiter=",")
#ncap = np.genfromtxt(path+"ncapprotons.csv", delimiter=",")
capprot = np.genfromtxt(path+"captureprotons.csv", delimiter=",")
print ("Total numbers")
print ("Capture: " + str(len(capture)))
print ("Decay: " + str(len(decay)))
#print ("Primaries: " + str(len(primaries)))
print ("Other: " + str(len(other)))
print ("Gamma: " + str(len(gamma)))
#print ("Protons: " + str(len(proton)))
print()
print("--------------------------------------")
print ("Quantities per Volume")
#print ("Decay SC1 " + str(len(sc1sc2(decay))))
print ("Decay SC2 " + str(len(decay_Sc2)))
print ("Gamma SC1 " + str(len(gamma_Sc1)))
print ("Gamma SC2 " + str(len(gamma_Sc2)))
print ("Ionization SC1 " + str(len(ioni_Sc1)))
print ("Ionization SC2 " + str(len(ioni_Sc2)))
print ("BoundDecay SC1 " + str(len(bound_Sc1)))
print ("BoundDecay SC2 " + str(len(bound_Sc2)))
#print ("Proton SC2 " + str(len(proton_Sc2)))
#print ("Proton SC1 " + str(len(proton_Sc1)))
print( "-------------------------------------")
print("Test:")
print(str(len(other_Sc1)+len(other_Sc2)))
print(str(len(sc1sc2(other)[1])+len(sc1sc2(other)[2])))

#print (len(decay) + len(primaries) + len(capture))
#print (len(decay))
#print (len(decay[decay[:, 6] == 0.]))


fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("SC1")
ax2.set_title("SC2")

ax1.set_xlabel("Zeit [ns]")
#ax1.set_ylabel("$\Delta E$ $[MeV]$")
ax1.set_ylabel("$E$ $[MeV]$")
ax2.set_xlabel("Zeit [ns]")
#ax2.set_ylabel("$\Delta E$ $[MeV]$")


ax1.set_xscale("log")
ax2.set_xscale("log")
ax1.set_yscale("log")
ax2.set_yscale("log")

#ax1.plot(primaries_Sc1[:, 1], primaries_Sc1[:, 2], 'b.', label="$\mu^+/\mu^-$", ms=3)
#ax2.plot(primaries_Sc2[:, 1], primaries_Sc2[:, 2], 'b.', label="$\mu^+/\mu^-$", ms=3)

ax1.set_xlim(0.01, 100000)
ax2.set_xlim(0.01, 100000)
ax1.set_ylim(0.0001, 100)
ax2.set_ylim(0.0001, 100)
ax1.plot(decay_Sc1[:, 1], decay_Sc1[:, 2], 'r.', label="$e^+/e^-$(freier Zerfall)", ms=3)
ax2.plot(decay_Sc2[:, 1], decay_Sc2[:, 2], 'r.', label="$e^+/e^-$(freier Zerfall)", ms=3)

ax1.plot(bound_Sc1[:, 1], bound_Sc1[:, 2], 'r.', label="$e^+/e^-$(gebundener Zerfall)", ms=3)
ax2.plot(bound_Sc2[:, 1], bound_Sc2[:, 2], 'r.', label="$e^+/e^-$(gebundener Zerrfall)", ms=3)

ax1.plot(proton_Sc1[:, 1], proton_Sc1[:, 2], 'g.', label="Protonen", ms=3)
ax2.plot(proton_Sc2[:, 1], proton_Sc2[:, 2], 'g.', label="Protonen", ms=3)

ax1.plot(ioni_Sc1[:, 1], ioni_Sc1[:, 2], 'g.', label="$e^+/e^-$(anderer Prozess)", ms=3)
ax2.plot(ioni_Sc2[:, 1], ioni_Sc2[:, 2], 'g.', label="$e^+/e^-$(anderer Prozess)", ms=3)

ax1.plot(other_Sc1[:, 1], other_Sc1[:, 2], 'g.', label="$e^+/e^-$(anderer Prozess)", ms=3)
ax2.plot(other_Sc2[:, 1], other_Sc2[:, 2], 'g.', label="$e^+/e^-$(anderer Prozess)", ms=3)

ax1.plot(capture_Sc1[:, 1], capture_Sc1[:, 2], 'b.', label="$e^-$(Einfang)", ms=3)
ax2.plot(capture_Sc2[:, 1], capture_Sc2[:, 2], 'b.', label="$e^-$(Einfang)", ms=3)

#ax1.axhline(y=0.0006, color='k', label="Schwelle")
#ax2.axhline(y=0.0006, color='k', label="Schwelle")
ax1.axvline(x=2000., color='k', linestyle="--", label="Schwelle")
ax2.axvline(x=2000., color='k', linestyle="--", label="Schwelle")

#ax1.plot(gamma_Sc1[:, 1], gamma_Sc1[:, 3], 'b.', label="Photonen", ms=3)
#ax2.plot(gamma_Sc2[:, 1], gamma_Sc2[:, 3], 'b.', label="Photonen", ms=3)

ax1.legend(loc=2)
ax2.legend(loc=2)
plt.tight_layout()
#plt.show()

