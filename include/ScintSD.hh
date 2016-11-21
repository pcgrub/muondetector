//
// Created by cgrubitz on 24.10.16.
//

#ifndef MUONDETECTOR_SCINTSD_HH
#define MUONDETECTOR_SCINTSD_HH

#include "G4VSensitiveDetector.hh"
#include "ScintHit.hh"

class G4Step;
class G4HCofThisEvent;
class G4TouchableHistory;


class ScintSD :public G4VSensitiveDetector{
public:
    ScintSD(G4String name);
    virtual ~ScintSD();

    virtual void Initialize(G4HCofThisEvent*HCE);
    virtual G4bool ProcessHits(G4Step*aStep, G4TouchableHistory*ROhist);

private:
    ScintHitsCollection* fHitsCollection;
    G4int fHCID;
};


#endif //MUONDETECTOR_SCINTSD_HH
