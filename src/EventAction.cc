//
// Created by cgrubitz on 24.10.16.
//

// Custom User classes
#include "EventAction.hh"
#include "ScintHit.hh"
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
#include "G4TrackingManager.hh"



EventAction::EventAction()
        : G4UserEventAction(),fSCID1(-1),fSCID2(-1), fNeutrinoFound(false)
{
    // print output for each event global setting
   // G4RunManager::GetRunManager()->SetPrintProgress(1);
}

EventAction::~EventAction() {}

void EventAction::BeginOfEventAction(const G4Event*) {
    if (fSCID1==-1) {
        G4SDManager* sdManager = G4SDManager::GetSDMpointer();
        // colletction init goes here like
        //fCUID = sdManager->GetCollectionID("/copper/CopperCol");
        fSCID1 = sdManager->GetCollectionID("scint1/ScintColl");
        fSCID2 = sdManager->GetCollectionID("scint2/ScintColl");


    }
}

void EventAction::EndOfEventAction(const G4Event* event) {
    //
    // some exception handling info
    G4HCofThisEvent* hce = event->GetHCofThisEvent();
    if (!hce) {

        G4ExceptionDescription msg;
        msg << "No hits collection of this event found.\n";
        G4Exception("EventAction::EndOfEventAction()",
                    "Code001", JustWarning, msg);
        return;
    }

    // initiate all hit collections in this manner:
    ScintHitsCollection* scintHC1
            = static_cast <ScintHitsCollection*>(hce->GetHC(fSCID1));
    ScintHitsCollection* scintHC2
            = static_cast <ScintHitsCollection*>(hce->GetHC(fSCID2));


    //CopperHitsCollection* copperHC
    //        = static_cast<CopperHitsCollection*>(hce->GetHC(fCUID));

    // some exception handling info:
    if ((!scintHC1) || (!scintHC2)){
        G4ExceptionDescription msg;
        msg << "something went wrong. Some Hits could not be found.\n";
        G4Exception("EventAction::EndOfEventAction()", "Code001", JustWarning, msg);

        return;
    }

    // do not write lines containing zero only
    if (scintHC1->entries()==0. && scintHC2->entries()==0.){return;}

    // Fill Histograms with all sorts of data
    // get the Analysis manager
    // I will do that later I guess
    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
    // fill Histograms
/*
    G4int n_hit = scintHC1->entries();
    analysisManager->FillH1(0, n_hit);

    for (G4int i=0;i<n_hit;i++)
        {
            ScintHit* first_hit = (*scintHC1)[i];
            G4double momentum = first_hit->GetMomentum();
            G4double theta = std::acos(momentum);
            analysisManager->FillH1(0, theta);
        }

*/

        // fill ntuples
    // fill the first columns reserved for the first Scintillator
    //G4cout<<  scintHC1->entries() << " Scint1 " <<  scintHC2->entries() << " Scint2 "<< G4endl;
    G4cout << "Event number: " << event->GetEventID() << G4endl;
    G4double E_temp = 0.;
    G4int Hit_number = 0;
    G4double Hit_Time = 0.;
    G4double Muon_Time = 0.;

    //time correction
    // to determine not the global time, but the time relative to the first muon hit
    // the muons_time must be found out first
    G4double Muon_Time_Sc1 = 0.;
    for (G4int i=0;i<scintHC1->entries();i++){
        if(((*scintHC1)[i]->GetName()=="mu+" ||(*scintHC1)[i]->GetName()=="mu-" )&& Muon_Time_Sc1 == 0.){
            Muon_Time_Sc1 = (*scintHC1)[i]->GetTime();
        }
    }
    G4double Muon_Time_Sc2 = 0.;
    for (G4int i=0;i<scintHC2->entries();i++){
        if(((*scintHC2)[i]->GetName()=="mu+" ||(*scintHC2)[i]->GetName()=="mu-" )&& Muon_Time_Sc2 == 0.){
            Muon_Time_Sc2 = (*scintHC2)[i]->GetTime();

            //Coincidence: throw away all data if a muon is detected in the second scint
            //return;
        }
    }
    Muon_Time = std::min(Muon_Time_Sc1,Muon_Time_Sc2);

    for (G4int i=0;i<scintHC1->entries();i++) {

        // The time is only measured if its the particle's first step in the medium
        if (Hit_number == 0){
            Hit_Time = (*scintHC1)[i]->GetTime();
        }

        //The hit is only generated at the last step so that each step the deposited energy can be added up

        // add up the energies until there is a new particle
        // a new particle is indicated by a new Track ID
        if ((i == scintHC1->entries()-1) || ((*scintHC1)[i+1]->GetTrack()!=(*scintHC1)[i]->GetTrack())){
            // column 0 event number
            analysisManager->FillNtupleDColumn(0, event->GetEventID());

            // column 1 Time
            analysisManager->FillNtupleDColumn(1, Hit_Time);

            // column 2 EnergySc1
            analysisManager->FillNtupleDColumn(2, E_temp+(*scintHC1)[i]->GetEnergy());

            // column 3 OriginalEnergySc1
            analysisManager->FillNtupleDColumn(3, (*scintHC1)[i]->GetOriginalKineticEnergy());

            // column 4 DecayFlagSc1
            G4String process = (*scintHC1)[i]->GetProcess();

            if (process == "Decay"){analysisManager->FillNtupleDColumn(4, 1.0);}
            else if (process == "muMinusCaptureAtRest") {
                if (fNeutrinoFound){analysisManager->FillNtupleDColumn(4, 3.0);}
                else {analysisManager->FillNtupleDColumn(4, 2.0);}
            }
            else if (process == "muIoni") {analysisManager->FillNtupleDColumn(4, 4.0); }
            else if (process == "muonNuclear"){ analysisManager->FillNtupleDColumn(4, 5.0);}
            else if (process == "photonNuclear"){ analysisManager->FillNtupleDColumn(4, 6.0);}
            else if (process == "protonInelastic"){ analysisManager->FillNtupleDColumn(4, 7.0);}
            else if (process == "neutronInelastic"){ analysisManager->FillNtupleDColumn(4, 8.0);}
            else {analysisManager->FillNtupleDColumn(4, 0.0);}

            // column 5 ParticeflagSc1
            G4String temp_name = (*scintHC1)[i]->GetName();
            if (temp_name == "e+") { analysisManager->FillNtupleDColumn(5, 1.0); }
            else if (temp_name == "e-") { analysisManager->FillNtupleDColumn(5, 2.0); }
            else if (temp_name == "mu+") { analysisManager->FillNtupleDColumn(5, 3.0); }
            else if (temp_name == "mu-") { analysisManager->FillNtupleDColumn(5, 4.0); }
            else if (temp_name == "proton") {analysisManager->FillNtupleDColumn(5, 5.0); }
            else if (temp_name == "neutron") {analysisManager->FillNtupleDColumn(5, 6.0);}
            else { analysisManager->FillNtupleDColumn(5, 0.0); }

            //column 6 Origin Volume
            G4String origin = (*scintHC1)[i]->GetOrigin();
            if (origin == "World") { analysisManager->FillNtupleDColumn(6, 0.0); }
            else if (origin == "Scint plate1") { analysisManager->FillNtupleDColumn(6, 1.0); }
            else if (origin == "Copper plate") { analysisManager->FillNtupleDColumn(6, 2.0); }
            else if (origin == "Scint plate2") { analysisManager->FillNtupleDColumn(6, 3.0); }
            else { analysisManager->FillNtupleDColumn(6, 0.0); }
            //G4cout << i << "times" << G4endl;

            // column 7 Scintillator number
            analysisManager->FillNtupleDColumn(7, 1.0);


            // column 8 Get a sense of the angular distribution
            G4double mom = (*scintHC1)[i]->GetMomentum();
            //G4double angle = -mom.getZ();
            //G4cout << "momz: " << mom  << G4endl;
            analysisManager->FillNtupleDColumn(8, mom);

            // column 9 Muon relative Time
            analysisManager->FillNtupleDColumn(9,Hit_Time-Muon_Time);

            // colunm 10 parent ID
            analysisManager->FillNtupleDColumn(10, (*scintHC1)[i]->GetParent());

            analysisManager->AddNtupleRow();

            // Fill the histograms for SC1
            if (temp_name == "e+" || temp_name == "e-"){
              if (process == "Decay"){analysisManager->FillH1(0, Hit_Time);}
              else if (process == "muMinusCaptureAtRest") {
                if (fNeutrinoFound){analysisManager->FillH1(2, Hit_Time);}
                else {analysisManager->FillH1(3, Hit_Time);}
              }
              else if (process == "muIoni"){analysisManager->FillH1(1, Hit_Time);}
            }
            else if (temp_name == "proton") {analysisManager->FillH1(4, Hit_Time);}
            else if (temp_name == "gamma") {analysisManager->FillH1(5, Hit_Time);}

            //reinit of temporary variables
            E_temp = 0.;
            Hit_number = 0;
        }
        else{
            E_temp+=(*scintHC1)[i]->GetEnergy();
            Hit_number++;
        }
    }
    // equivalent scenario as in scint1
    for (G4int i=0;i<scintHC2->entries();i++) {

        if (Hit_number == 0) {
            Hit_Time = (*scintHC2)[i]->GetTime();
        }
        //G4cout << event->GetEventID() << " event " << " Eorg " << E_temp << " E temp " <<i <<" times"<< G4endl;
        if (i == scintHC2->entries() - 1 || ((*scintHC2)[i+1]->GetTrack()!=(*scintHC2)[i]->GetTrack())) {
            // column 0 event number
            analysisManager->FillNtupleDColumn(0, event->GetEventID());
            // column 1 Time
            analysisManager->FillNtupleDColumn(1, Hit_Time);
            // column 2 EnergySc2
            analysisManager->FillNtupleDColumn(2, E_temp+(*scintHC2)[i]->GetEnergy());
            // column 3 OriginalEnergySc2
            analysisManager->FillNtupleDColumn(3, (*scintHC2)[i]->GetOriginalKineticEnergy());

            G4String process = (*scintHC2)[i]->GetProcess();
            // column 4 DecayFlagSc2
            if (process == "Decay") { analysisManager->FillNtupleDColumn(4, 1.0); }
            else if (process == "muMinusCaptureAtRest") {
                if (fNeutrinoFound){analysisManager->FillNtupleDColumn(4, 3.0);}
                else {analysisManager->FillNtupleDColumn(4, 2.0);}
            }
            else if (process == "muIoni") {analysisManager->FillNtupleDColumn(4, 4.0); }
            else if (process == "muonNuclear"){ analysisManager->FillNtupleDColumn(4, 5.0);}
            else if (process == "photonNuclear"){ analysisManager->FillNtupleDColumn(4, 6.0);}
            else if (process == "protonInelastic"){ analysisManager->FillNtupleDColumn(4, 7.0);}
            else if (process == "neutronInelastic"){ analysisManager->FillNtupleDColumn(4, 8.0);}
            else { analysisManager->FillNtupleDColumn(4, 0.0); }

            // column 5 ParticeflagSc2
            G4String temp_name = (*scintHC2)[i]->GetName();
            if (temp_name == "e+") { analysisManager->FillNtupleDColumn(5, 1.0); }
            else if (temp_name == "e-") { analysisManager->FillNtupleDColumn(5, 2.0); }
            else if (temp_name == "mu+") { analysisManager->FillNtupleDColumn(5, 3.0); }
            else if (temp_name == "mu-") { analysisManager->FillNtupleDColumn(5, 4.0); }
            else if (temp_name == "proton") {analysisManager->FillNtupleDColumn(5, 5.0);}
            else if (temp_name == "neutron") {analysisManager->FillNtupleDColumn(5, 6.0);}
            else { analysisManager->FillNtupleDColumn(5, 0.0); }

            // column 6
            G4String origin = (*scintHC2)[i]->GetOrigin();
            if (origin == "World") { analysisManager->FillNtupleDColumn(6, 0.0); }
            else if (origin == "Scint plate1") { analysisManager->FillNtupleDColumn(6, 1.0); }
            else if (origin == "Copper plate") { analysisManager->FillNtupleDColumn(6, 2.0); }
            else if (origin == "Scint plate2") { analysisManager->FillNtupleDColumn(6, 3.0); }
            else { analysisManager->FillNtupleDColumn(6, 0.0); }

            //column 7
            //scintillator
            analysisManager->FillNtupleDColumn(7, 2.0);

            //column 8
            G4double mom = (*scintHC2)[i]->GetMomentum();
            analysisManager->FillNtupleDColumn(8, mom);

            //column 9 Muon relative Time
            analysisManager->FillNtupleDColumn(9,Hit_Time-Muon_Time);

            // colunm 10 parent ID
            analysisManager->FillNtupleDColumn(10, (*scintHC2)[i]->GetParent());

            analysisManager->AddNtupleRow();

            // Fill the histograms for SC2
            if (temp_name == "e+" || temp_name == "e-"){
              if (process == "Decay"){analysisManager->FillH1(6, Hit_Time);}
              else if (process == "muMinusCaptureAtRest") {
                if (fNeutrinoFound){analysisManager->FillH1(8, Hit_Time);}
                else {analysisManager->FillH1(9, Hit_Time);}
              }
              else if (process == "muIoni"){analysisManager->FillH1(7, Hit_Time);}
            }
            else if (temp_name == "proton") {analysisManager->FillH1(10, Hit_Time);}
            else if (temp_name == "gamma") {analysisManager->FillH1(11, Hit_Time);}

            // reinit the values used for
            E_temp = 0.;
            Hit_number = 0;

        }
        else{
            E_temp+=(*scintHC2)[i]->GetEnergy();
            Hit_number++;
        }

    }
    // Reset the Neutrino search from SteppingAction
    // because it can not be reset there
    fNeutrinoFound = false;
}
