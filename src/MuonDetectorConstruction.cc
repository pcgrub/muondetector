//
// Created by cgrubitz on 13.10.16.
//

#include "MuonDetectorConstruction.hh"
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


#include "G4UserLimits.hh"
#include "ScintSD.hh"

// Constructor

MuonDetectorConstruction::MuonDetectorConstruction():
        G4VUserDetectorConstruction(),ScintLog1(0),ScintLog2(0),CopperLog(0), fStepLimit(NULL){
}

MuonDetectorConstruction::~MuonDetectorConstruction()
{
    delete fStepLimit;
}


//Definitions of Materials used for the Detector


G4VPhysicalVolume*MuonDetectorConstruction::Construct() {


    G4NistManager* man = G4NistManager::Instance();

    // All of these materials come from the predefined
    // Geant4-database using data from NIST

    // define element copper
    G4Material* Cu = man->FindOrBuildMaterial("G4_Cu");

    //define material air:
    G4Material* air = man->FindOrBuildMaterial("G4_AIR");

    // define polyvinyltoluene scintillator material:
    G4Material* scintillator = man->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");
    //G4Material* concrete = man->FindOrBuildMaterial("G4_CONCRETE");


    G4bool checkOverlaps = true;
    // all the parts and properties of the detector components go here
    // everything containing world is an overall property of the room
    //first attempt of solid (some sort of shape object)
    // later to be used in a logical volume

    // dimensions of a copperplate or scintillator (they are identical):
    G4double PlattenDimX = 60.0*cm;
    G4double PlattenDimY = 36.0*cm;
    G4double PlattenDimZ = 1.0*cm;

    // the whole room is a cube for now:
    G4double WorldDimX_Y = 70.0*cm;
    G4double WorldDimZ = 70.0*cm;

    // every shape in this detector is a box shape
    // the different shaped boxes are initialized here
    G4Box* WorldBox = new G4Box("World", 0.5* WorldDimX_Y, 0.5* WorldDimX_Y, 0.5* WorldDimZ);

    // shape of both the scintillator and the copper plates
    G4Box* common_shape = new G4Box("Platte", 0.5*PlattenDimX, 0.5*PlattenDimY, 0.5*PlattenDimZ);

    //G4Box* concrete_box = new G4Box("Betonform", 0.75*m, 0.75*m, 0.75*m);

    // create a logical volume:
    // give the shape a material

    G4LogicalVolume* WorldLog = new G4LogicalVolume(WorldBox, air, "World");


    ScintLog1 = new G4LogicalVolume(common_shape, scintillator, "Scint plate1");
    CopperLog = new G4LogicalVolume(common_shape, Cu, "Copper plate");
    ScintLog2 = new G4LogicalVolume(common_shape, scintillator, "Scint plate2");
    //G4LogicalVolume* ConcreteLog = new G4LogicalVolume(concrete_box, concrete,"concrete");

    // create a physical volume:
    // put your plate somewhere in the room(world):
    G4double posOVERALL_x = 0.0*meter;
    G4double posOVERALL_y = 0.0*meter;


    new G4PVPlacement(0,              // no rotation
                      G4ThreeVector(posOVERALL_x, posOVERALL_y, 0.*cm),
            //translation
                      ScintLog1,      //corresponding logical volume
                      "1-SC1",  // the name of the volume
                      WorldLog,      // its mother log volume
                      false,         // no boolean operations
                      0,
                      checkOverlaps);            // its copy number
    // there are two plates

     new G4PVPlacement(0,              // no rotation
                     G4ThreeVector(posOVERALL_x, posOVERALL_y, 3.1*cm),
            //translation
                     CopperLog,      //corresponding logical volume
                     "2-Copper1",  // the name of the volume
                     WorldLog,       // its mother log volume
                     false,          // no boolean operations
                     0,
                      checkOverlaps);             // its copy number

    new G4PVPlacement(0,              // no rotation
                     G4ThreeVector(posOVERALL_x, posOVERALL_y, 4.1*cm),
            //translation
                     CopperLog,      //corresponding logical volume
                     "3-Copper2",  // the name of the volume
                     WorldLog,       // its mother log volume
                     false,          // no boolean operations
                     1,
                      checkOverlaps);             // its copy number



    new G4PVPlacement(0,              // no rotation
                      G4ThreeVector(posOVERALL_x, posOVERALL_y, 6.4*cm),
            //translation
                      ScintLog2,      //corresponding logical volume
                      "4-SC2",  // the name of the volume
                      WorldLog,      // its mother log volume
                      false,         // no boolean operations
                      0,
                      checkOverlaps);            // its copy number

    // the physical volume for the "world" is always initialized in
    // the following manner:
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

    // Tracking cuts to make sure that there are enough trajectory steps in certain volumes
    G4double maxStep = 0.1*PlattenDimZ;
    fStepLimit = new G4UserLimits(maxStep);
    CopperLog->SetUserLimits(fStepLimit);
    ScintLog1->SetUserLimits(fStepLimit);
    ScintLog2->SetUserLimits(fStepLimit);


    return worldPV;
}

void MuonDetectorConstruction::ConstructSDandField() {
    // sensitive detectors -----------------------------------------------------
    G4SDManager* SDman = G4SDManager::GetSDMpointer();
    G4String SDname;


    G4VSensitiveDetector* scintillator1 = new ScintSD(SDname="/scint1");
    SDman->AddNewDetector(scintillator1);
    ScintLog1->SetSensitiveDetector(scintillator1);

    G4VSensitiveDetector* scintillator2 = new ScintSD(SDname="/scint2");
    SDman->AddNewDetector(scintillator2);
    ScintLog2->SetSensitiveDetector(scintillator2);
}
//