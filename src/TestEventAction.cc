//
// Created by piet on 14.11.16.
//

#include "../include/TestEventAction.hh"


#include "ScintHit.hh"
#include "CopperHit.hh"
#include "Analysis.hh"

// geant4 classes
#include "G4Event.hh"
#include "G4RunManager.hh"
#include "G4EventManager.hh"
#include "G4HCofThisEvent.hh"
#include "G4VHitsCollection.hh"
#include "G4SDManager.hh"
#include "G4SystemOfUnits.hh"
#include "G4ios.hh"


TestEventAction::TestEventAction()
        : G4UserEventAction(),fSCID1(-1)
{
    // print output for each event global setting
    // G4RunManager::GetRunManager()->SetPrintProgress(1);
}

TestEventAction::~TestEventAction() {}

void TestEventAction::BeginOfEventAction(const G4Event*) {
    if (fSCID1==-1) {
        G4SDManager *sdManager = G4SDManager::GetSDMpointer();
        // colletction init goes here like
        //fCUID = sdManager->GetCollectionID("/copper/CopperCol");
        fSCID1 = sdManager->GetCollectionID("scint1/ScintColl");
    }
}
void TestEventAction::EndOfEventAction(const G4Event* event) {

        // some exception handling info
        G4HCofThisEvent *hce = event->GetHCofThisEvent();
        ScintHitsCollection* scintHC1
            = static_cast <ScintHitsCollection*>(hce->GetHC(fSCID1));

    if (scintHC1->entries()==0.){return;}

    // Fill Histograms with all sorts of data
    // get the Analysis manager
    // I will do that later I guess
    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();

    G4cout << "Event number: " << event->GetEventID() << G4endl;
    for (G4int i=0;i<scintHC1->entries();i++) {
        //G4cout <<event->GetEventID() << " event "<<  " Eorg " << E_temp << " E temp " <<i <<" times"<< G4endl;
        // add up the energies until there is a new particle
        // a new particle is indicated by the
        if ((i == scintHC1->entries()-1) || ((*scintHC1)[i+1]->GetTrack()!=(*scintHC1)[i]->GetTrack())) {
            analysisManager->FillNtupleDColumn(3, (*scintHC1)[i]->GetOriginalKineticEnergy());

            // column 5 ParticeflagSc1
            G4String temp_name = (*scintHC1)[i]->GetName();
            if (temp_name == "e+") { analysisManager->FillNtupleDColumn(5, 1.0); }
            else if (temp_name == "e-") { analysisManager->FillNtupleDColumn(5, 2.0); }
            else if (temp_name == "mu+") { analysisManager->FillNtupleDColumn(5, 3.0); }
            else if (temp_name == "mu-") { analysisManager->FillNtupleDColumn(5, 4.0); }
            else { analysisManager->FillNtupleDColumn(5, 0.0); }

            G4double mom = (*scintHC1)[i]->GetMomentum();
            //G4double angle = -mom.getZ();
            //G4cout << "momz: " << mom  << G4endl;
            analysisManager->FillNtupleDColumn(8, mom);

            analysisManager->AddNtupleRow();
        }

    }

}

