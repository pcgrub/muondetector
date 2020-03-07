# Muon Detector
This repository provides a fully functional Geant4 Simulation of a muon detector. For more details see [my bachelor thesis](https://iktp.tu-dresden.de/IKTP/pub/16/Grubitz_Clemens_Bachelorarbeit.pdf)

## Dependencies
Geant4 10.2 or higher, ROOT

## Usage

### Compiling

In order to compile the code succesfully, Geant4 has to be running in the shell.
`$ source /PATH/TO/geant4/bin/geant4.sh`

Compiling the code with N being the number of available threads/cores  

`$ cd /path/to/muondetector`  
`$ mkdir ../build-muondetector`  
`$ cd ../build-muondetector`  
`$ cmake -DGeant4_DIR=/PATH/TO/geat4/ /path/to/muondetector`  
`$ make -jN`  

### Running the Simulation

Running the simulation without a graphical output.  
`$ cd /path/to/build-muondetector`  
`$ ./MuonDetector run.mac`  
