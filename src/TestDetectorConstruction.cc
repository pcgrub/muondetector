//
// Created by piet on 14.11.16.
//

#include "../include/TestDetectorConstruction.hh"

#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4Tubs.hh"
#include "G4Sphere.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4RotationMatrix.hh"
#include "G4Transform3D.hh"
#include "G4SDManager.hh"
#include "G4MultiFunctionalDetector.hh"
#include "G4VPrimitiveScorer.hh"
#include "G4PSEnergyDeposit.hh"
#include "G4PSDoseDeposit.hh"
#include "G4VisAttributes.hh"
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"

#include "ScintSD.hh"


TestDetectorConstruction::TestDetectorConstruction():
        G4VUserDetectorConstruction(),ScintLog1(0){
}

TestDetectorConstruction::~TestDetectorConstruction()
{}

G4VPhysicalVolume*TestDetectorConstruction::Construct() {


    G4NistManager *man = G4NistManager::Instance();

    G4bool checkOverlaps=true;
    //define material air:
    G4Material* air = man->FindOrBuildMaterial("G4_AIR");

    // define polyvinyltoluene scintillator material:
    G4Material* scintillator = man->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");

    G4Material* concrete = man->FindOrBuildMaterial("G4_CONCRETE");

    // the whole room is a cube for now:
    G4double WorldDimX_Y = 200.0*cm;
    G4double WorldDimZ = 400.0*cm;

    // every shape in this detector is a box shape
    // the different shaped boxes are initialized here
    G4Box* WorldBox = new G4Box("World", 0.5* WorldDimX_Y, 0.5* WorldDimX_Y, 0.5* WorldDimZ);
    G4Box* concrete_box = new G4Box("Betonform", 0.75*m, 0.75*m, 0.75*m);
    //G4Sphere* angular_tube = new G4Sphere("Winkelkugel", 3.*cm, 8.*cm, 0.*deg, 360.*deg, 0.*deg, 180.*deg);
    G4Box* concrete_detector_box = new G4Box("BetonDetektorform", 0.75*m, 0.75*m, 0.5*cm);
    // logical volumes for testing purposes
    G4LogicalVolume* WorldLog = new G4LogicalVolume(WorldBox, air, "World");
    G4LogicalVolume* ConcreteLog = new G4LogicalVolume(concrete_box, concrete,"concrete");
    //ScintLog1 = new G4LogicalVolume(angular_tube, scintillator, "KugelLog");

    ScintLog1 = new G4LogicalVolume(concrete_detector_box, scintillator, "BetonDetektorLog");
    new G4PVPlacement(0,              // no rotation
                      G4ThreeVector(0., 0., -13.*cm),
            //translation
                      ScintLog1,      //corresponding logical volume
                      "Betondetektor",  // the name of the volume
                      WorldLog,      // its mother log volume
                      false,         // no boolean operations
                      0,
                      checkOverlaps);

    new G4PVPlacement(0,              // no rotation
                      G4ThreeVector(0. , 0., -90.*cm),
            //translation
                      ConcreteLog,      //corresponding logical volume
                      "concrete-physical",  // the name of the volume
                      WorldLog,      // its mother log volume
                      false,         // no boolean operations
                      0,
                      checkOverlaps);            // its copy number


    G4VPhysicalVolume* worldPV
            = new G4PVPlacement(
                    0,               // no rotation
                    G4ThreeVector(), // at (0,0,0)
                    WorldLog,         // its logical volume
                    "World",         // its name
                    0,               // its mother  volume
                    false,           // no boolean operations
                    0,               // copy number
                    1); // checking overlaps

    return worldPV;
}

void TestDetectorConstruction::ConstructSDandField() {
    // sensitive detectors -----------------------------------------------------
    G4SDManager *SDman = G4SDManager::GetSDMpointer();
    G4String SDname;


    G4VSensitiveDetector *scintillator1 = new ScintSD(SDname = "/scint1");
    SDman->AddNewDetector(scintillator1);
    ScintLog1->SetSensitiveDetector(scintillator1);
}