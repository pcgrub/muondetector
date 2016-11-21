//
// Created by cgrubitz on 27.10.16.
//

#include "../include/CopperSD.hh"

#include "G4HCofThisEvent.hh"
#include "G4TouchableHistory.hh"
#include "G4Track.hh"
#include "G4Step.hh"
#include "G4SDManager.hh"
#include "G4ios.hh"

CopperSD::CopperSD(G4String name)
        : G4VSensitiveDetector(name), fHitsCollection(0), fHCID(-1)
{
    G4String HCname = "CopperColl";
    collectionName.insert(HCname);
}

CopperSD::~CopperSD() {}

void CopperSD::Initialize(G4HCofThisEvent* hce) {
    fHitsCollection = new CopperHitsCollection
            (SensitiveDetectorName,collectionName[0]);
    if (fHCID<0)
    { fHCID = G4SDManager::GetSDMpointer()->GetCollectionID(fHitsCollection); }
    hce->AddHitsCollection(fHCID,fHitsCollection);
}

G4bool CopperSD::ProcessHits(G4Step* step, G4TouchableHistory*) {
    G4double edep = step->GetTotalEnergyDeposit();
    if (edep ==0.) return true;

    G4StepPoint* preStepPoint = step->GetPreStepPoint();

    G4TouchableHistory* touchable =
            (G4TouchableHistory*)(preStepPoint->GetTouchable());
    G4int copyNo = touchable->GetVolume()->GetCopyNo();
    G4double hitTime = preStepPoint->GetGlobalTime();

    for (G4int i=0;i<fHitsCollection->entries();i++)
    {
        CopperHit* hit = new CopperHit(copyNo,hitTime, edep);
        fHitsCollection->insert(hit);
    }
    return true;
}
