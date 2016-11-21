//
// Created by cgrubitz on 27.10.16.
//

#ifndef MUONDETECTOR_COPPERSD_HH
#define MUONDETECTOR_COPPERSD_HH

#include "G4VSensitiveDetector.hh"
#include "CopperHit.hh"

class G4Step;
class G4HCofThisEvent;
class G4TouchableHistory;


class CopperSD :public G4VSensitiveDetector{
public:
    CopperSD(G4String name);
    virtual ~CopperSD();

    virtual void Initialize(G4HCofThisEvent*HCE);
    virtual G4bool ProcessHits(G4Step*aStep, G4TouchableHistory*ROhist);

private:
    CopperHitsCollection* fHitsCollection;
    G4int fHCID;
};

#endif //MUONDETECTOR_COPPERSD_HH
