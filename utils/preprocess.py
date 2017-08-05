import numpy as np

path = "/home/piet/Dokumente/build-testmuon/"

data0 = np.genfromtxt(path+"muon_Hits_nt_data_t0.csv", delimiter=",")
data1 = np.genfromtxt(path+"muon_Hits_nt_data_t1.csv", delimiter=",")
data2 = np.genfromtxt(path+"muon_Hits_nt_data_t2.csv", delimiter=",")
data3 = np.genfromtxt(path+"muon_Hits_nt_data_t3.csv", delimiter=",")
m = np.concatenate((data0, data1, data2, data3))


electrons = m[np.logical_or((m[:, 5] == 1),(m[:,5] == 2))]
muons = m[np.logical_or((m[:, 5] == 3),(m[:,5] == 4))]
protons = m[m[:,5] == 5]
gamma = m[m[:,5] == 0]

ncap = protons[protons[:,4]== 5]
captureprot = protons[protons[:,4]== 2]
otherprot = protons[np.logical_and((protons[:,4]!= 5),(protons[:,4]!=2))]

decay = electrons[electrons[:, 4] == 1]
capture = electrons[electrons[:, 4] == 2]
bound = electrons[electrons[:, 4] == 3]
ioni = electrons[electrons[:, 4] == 4]
other = electrons[electrons[:, 4] == 0]

print("Whole data set: " + str(len(m)))
print("Electrons: " + str(len(electrons)))
print("Muons: " + str(len(muons)))
print("Protons: " + str(len(protons)))
print("Photons: " + str(len(gamma)))

np.savetxt(path+"decayelectrons.csv", decay, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"capturedelectrons.csv", capture, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"muons.csv", muons, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"ncapprotons.csv", ncap, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"captureprotons.csv", captureprot, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"otherprot.csv", otherprot, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"gamma.csv", gamma, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"otherelectrons.csv", other, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"bounddecayelectrons.csv", bound, delimiter=",", fmt="%7.7f", newline="\n")
np.savetxt(path+"ionizationelectrons.csv", ioni, delimiter=",", fmt="%7.7f", newline="\n")

