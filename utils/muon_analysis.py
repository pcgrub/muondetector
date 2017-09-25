from matplotlib import pyplot as plt
import numpy as np
import time as t


def sc1sc2(mat, column=7):
    """seperates input array for copper, scint1 and scint2 for volume in
    which detected for column=7 or origin volume column=6"""
    if (column==6):
        return  mat[mat[:, column] == 1], mat[mat[:, column] == 3], mat[mat[:, column] == 2]
    return  mat[mat[:, column] == 1], mat[mat[:, column] == 2], mat[mat[:, column] == 3]


def timecoumn(mat):
    return mat[:,1]


def write_analysis_file(data,CreationType):

    VolumeType = np.array(["SC1", "SC2", "Cu"])

    now = t.strftime("%Y-%m-%dT%H:%M:%SZ")
    f = open(path+"muondetector_analysis.txt", "w")
    f.write("Muon detector analysis from " + path + "\n")
    f.write("finished at " + now + "\n")
    f.write("\n")
    f.write("\n")
    f.write ("Total numbers by detector\n")
    f.write ("----------------------------------------\n")
    for i in range(len(CreationType)):
        if data[i] is not None:
            for d in range(len(VolumeType)):
                f.write(CreationType[i]+ " " + VolumeType[d] + ": " + str(len(sc1sc2(data[i])[d]))+ "\n")
                f.write("----------------------------------------\n")

    f.write ("****************************************\n")
    f.write ("Total numbers by origin\n")
    f.write ("----------------------------------------\n")
    for i in range(len(CreationType)):
        if data[i] is not None:
            for d in range(len(VolumeType)):
                f.write(CreationType[i]+ " " + VolumeType[d] + ": " + str(len(sc1sc2(data[i], column=6)[d]))+"\n")
                f.write("----------------------------------------\n")
    f.close()

#read in files
path = "/Users/piet/Documents/build-muondetector/"


data = np.empty(14, dtype=np.ndarray)
# 0 decay electrons/positrons
data[0]= np.genfromtxt(path+"decayelectrons.csv", delimiter=",")

# 1 Capture electrons
data[1] = np.genfromtxt(path+"capturedelectrons.csv", delimiter=",")

# 2 primary particles(muons)
# data[2] = np.genfromtxt(path+"muons.csv", delimiter=",")

# 3 electrons from showers
data[3] = np.genfromtxt(path+"otherelectrons.csv", delimiter=",")

# 4 photons
data[4] = np.genfromtxt(path+"gamma.csv", delimiter=",")

# 5 electrons from ionization
data[5] = np.genfromtxt(path+"ionizationelectrons.csv", delimiter=",")

# 6 electrons from bound decay
data[6] = np.genfromtxt(path+"bounddecayelectrons.csv", delimiter=",")

#  7 Protons from muonNuclear
data[7] = np.genfromtxt(path+"muonNuclear.csv", delimiter=",")

# 8 Protons from photon nuclear
data[8] = np.genfromtxt(path+"photonNuclear.csv", delimiter=",")

# 9 Protons from proton Inelastic
data[9] = np.genfromtxt(path+"protonInelastic.csv", delimiter=",")

# 10 protons from neutron Inelastic
data[10] = np.genfromtxt(path+"neutronInelastic.csv", delimiter=",")

# 11 Protons from muon capture
data[11] = np.genfromtxt(path+"captureprotons.csv", delimiter=",")

# 12 protons from other processes
data[12] = np.genfromtxt(path+"otherprot.csv", delimiter=",")

# 13 neutrons
data[13] = np.genfromtxt(path+"neutron.csv", delimiter=",")

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("SC1")
ax2.set_title("SC2")

ax1.set_xlabel("Zeit [ns]")
ax2.set_xlabel("Zeit [ns]")

CreationType = np.array(["$e^+/e^-$ decay", "electron from muon capture", "muons",
                         "shower electron", "gamma",
                         "electron from ionization", "electron from bound decay",
                         "proton from muonNuclear", "proton from photonNuclear",
                         "proton from protonInelastic", "proton from neutronInelastic",
                         "proton from muonCapture",
                         "proton from hadElastic", "neutron"])


nmax = 2500
tmax = 10000
ax1.set_xlim((0,tmax))
ax1.set_ylim((0,nmax))
ax2.set_xlim((0,tmax))
ax2.set_ylim((0,nmax))

n = 100
bins = np.linspace(0.,tmax, n+1)

#decay
stuff_to_plot =[0,1,4,5,6,7,8,9,10,11,12]
stack_SC1 = []
stack_SC2 = []
stack_label = []
for i,val in enumerate(stuff_to_plot):
    stack_SC1.append(sc1sc2(data[val])[0][:, 1])
    stack_SC2.append(sc1sc2(data[val])[1][:, 1])
    stack_label.append(CreationType[val])


ax1.hist(stack_SC1, bins, label=stack_label, stacked=True)
ax2.hist(stack_SC2, bins, label=stack_label, stacked=True)


print("normal decay")
dec_times = np.append(sc1sc2(data[0])[0][:,1],sc1sc2(data[0])[0][:,1])
print(np.mean(dec_times))
print (np.std(dec_times)/np.sqrt(len(dec_times)))

times = np.append(sc1sc2(data[6])[0][:,1],sc1sc2(data[6])[0][:,1])
rel = times[times>10]

print ("bound decay mean and error: ")
print(np.mean(rel)-10)
print(np.std(rel)/np.sqrt(len(rel))) 


print ("proton mean and error: ")
prot_times = np.append(sc1sc2(data[12])[0][:,1],sc1sc2(data[12])[0][:,1])
print(np.mean(prot_times))
print(np.std(prot_times)/np.sqrt(len(prot_times))) 

ax1.legend(loc=1)
ax2.legend(loc=1)
plt.tight_layout()
plt.show()

