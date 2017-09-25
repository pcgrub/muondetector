//
// Created by piet on 27.04.17.
//

#include "SteppingAction.hh"
//#include "Run.hh"
#include "EventAction.hh"
//#include "HistoManager.hh"
#include "G4RunManager.hh"
#include "G4SteppingManager.hh"
#include "G4VProcess.hh"
#include "G4UnitsTable.hh"

// constructor
SteppingAction::SteppingAction(EventAction* event) : G4UserSteppingAction(), fEventAction(event) {}

void SteppingAction::UserSteppingAction(const G4Step* aStep) {
    G4ParticleDefinition* particle = aStep->GetTrack()->GetDefinition();
    const G4TrackVector* secondary = fpSteppingManager->GetSecondary();
    for (size_t lp=0; lp<(*secondary).size(); lp++){
        particle = (*secondary)[lp]->GetDefinition();
        G4String name = particle->GetParticleName();
        if (name=="anti_nu_e") {
            G4String process = (*secondary)[lp]->GetCreatorProcess()->GetProcessName();
            if (process == "muMinusCaptureAtRest") fEventAction->SetNeutrinoFound(true);
        }
    }
}
