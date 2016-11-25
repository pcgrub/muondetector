//
// Created by cgrubitz on 24.10.16.
//

#include "ScintSD.hh"

#include "ScintHit.hh"

#include "G4HCofThisEvent.hh"
#include "G4TouchableHistory.hh"
#include "G4Track.hh"
#include "G4Step.hh"
#include "G4SDManager.hh"
#include "G4ios.hh"
#include "G4VProcess.hh"
#include "G4VRestProcess.hh"


ScintSD::ScintSD(G4String name)
        : G4VSensitiveDetector(name), fHitsCollection(0), fHCID(-1)
{
    G4String HCname = "ScintColl";
    collectionName.insert(HCname);
}

ScintSD::~ScintSD() {}

void ScintSD::Initialize(G4HCofThisEvent* hce) {
    fHitsCollection = new ScintHitsCollection
            (SensitiveDetectorName,collectionName[0]);
    if (fHCID<0)
    { fHCID = G4SDManager::GetSDMpointer()->GetCollectionID(fHitsCollection); }
    hce->AddHitsCollection(fHCID,fHitsCollection);
}

G4bool ScintSD::ProcessHits(G4Step* step, G4TouchableHistory*) {

    // acces track history from the particle caught
    G4Track* track = step->GetTrack();

    // access info from step and track
    G4double edep = step->GetTotalEnergyDeposit();

    // some timesaving measures
    if (edep ==0.) return true;

    // useful information of creation process, particle name and so on

    // also changed for testing purposes
    G4double orEn = track->GetVertexKineticEnergy();
    //G4double orEn = track->GetTotalEnergy();

    //
    const G4LogicalVolume* originvol = track->GetLogicalVolumeAtVertex();
    G4ParticleDefinition* particle = track->GetDefinition();
    G4int trackID = track->GetTrackID();


    // extracting the creation process from primary particles results  in a crash
    G4String name = particle->GetParticleName();
    G4String process;
    if (name == "mu+" || name =="mu-") {
        process = "None";
    }
    else {
        const G4VProcess* creation = track->GetCreatorProcess();
        G4VRestProcess* a;
        G4double b = a->GetMeanLifeTime(const track*, const step*);
        process = creation->GetProcessName();
        if (process == "muMinusCaptureAtRest"){
            //G4cout << creation->GetMeanLifeTime() << "ns lifetime" << G4endl;
        }
    }

    G4String origin = originvol->GetName();


    G4ThreeVector Momentum = track->GetVertexMomentumDirection();
    //G4cout << "z: " << Momentum.z() << G4endl;
    //time extraction from previous step
    G4StepPoint* preStepPoint = step->GetPreStepPoint();

    // not entirely sure whether I need that
    G4TouchableHistory* touchable =
            (G4TouchableHistory*)(preStepPoint->GetTouchable());
    G4VPhysicalVolume* physical = touchable->GetVolume();

    //insert the hits of ScintHit type
    // changed for testing purpose:
    if (/*name == "e+" || name == "e-" || name=="gamma" ||*/ name == "mu+" || name == "mu-") {
        ScintHit *hit = new ScintHit(name, edep, origin, orEn, process, trackID, Momentum.z());
        hit->SetLogV(physical->GetLogicalVolume());
        hit->SetTime(preStepPoint->GetGlobalTime());
        //hit->Print();
        fHitsCollection->insert(hit);
    }
    return true;
}

