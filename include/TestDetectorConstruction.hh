//
// Created by piet on 14.11.16.
//

#ifndef MUONDETECTOR_TESTDETECTORCONSTRUCTION_HH
#define MUONDETECTOR_TESTDETECTORCONSTRUCTION_HH



#include "G4VUserDetectorConstruction.hh"
#include "globals.hh"

class G4VPhysicalVolume;
class G4LogicalVolume;

// Define a detectorConstruction class

class TestDetectorConstruction: public G4VUserDetectorConstruction {
public:
    TestDetectorConstruction();

    virtual ~TestDetectorConstruction();

public:
    virtual G4VPhysicalVolume *Construct();

    virtual void ConstructSDandField();

    G4LogicalVolume *ScintLog1;
};

#endif //MUONDETECTOR_TESTDETECTORCONSTRUCTION_HH