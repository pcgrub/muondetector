import numpy as np
from matplotlib import pyplot as plt

path1 = '../measurement/20151127.txt'
path2 = '../measurement/201618.11.txt'
path = '/Users/piet/Documents/build-muondetector/'
# decay electrons/positrons
decay = np.genfromtxt(path+"decayelectrons.csv", delimiter=",")

# electrons from bound decay
bound = np.genfromtxt(path+"bounddecayelectrons.csv", delimiter=",")

data1 = np.genfromtxt(path1,skip_header=85, delimiter='\t')
data2 = np.genfromtxt(path2,skip_header=85, delimiter='\t')

bin_width = 41.7
N = 256.

bins = np.linspace(0, N*bin_width, N+1)
bin_mids = bins[1:] - bin_width/2.

title = 'Messungen'
fig = plt.figure(num=title)

ax1 = fig.add_subplot(111)
boom = []
boom.append(decay[:,1])
boom.append(bound[:, 1])

labels = ['freier Zerfall Sim', 'freier Zerfall + gebundener Zerfall Sim']

ax1.hist(boom, bins=bins, histtype='step', label=labels, stacked=True)

ax1.plot(bin_mids, data2[:, 1], ls='steps', color='g', label='Messung 2016')
ax1.plot(bin_mids, data1[:, 1], ls='steps', color='r', label='Messung 2015')

ax1.set_ylabel('# Anzahl Ereignisse')
ax1.set_xlabel('Zeit [ns]')

plt.legend(loc=1)
plt.show()
