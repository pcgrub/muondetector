//
// Created by cgrubitz on 13.10.16.
//

#ifndef GEANT4_DETECTOR_GEOMETRY_H
#define GEANT4_DETECTOR_GEOMETRY_H


#include "G4VUserDetectorConstruction.hh"
#include "globals.hh"

// useful classes for the main program
class G4VPhysicalVolume;
class G4LogicalVolume;

// Define a detectorConstruction class

class MuonDetectorConstruction: public G4VUserDetectorConstruction
{
public:
    MuonDetectorConstruction();
    virtual ~MuonDetectorConstruction();

public:
    virtual G4VPhysicalVolume* Construct();
    virtual void ConstructSDandField();
    G4LogicalVolume* ScintLog1;
    G4LogicalVolume* ScintLog2;
    G4LogicalVolume* CopperLog;

};


#endif //GEANT4_DETECTOR_GEOMETRY_H
