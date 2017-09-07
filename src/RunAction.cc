//
// Created by cgrubitz on 27.10.16.
//

#include "../include/RunAction.hh"

#include "Analysis.hh"

#include "G4UnitsTable.hh"
#include "G4SystemOfUnits.hh"

RunAction::RunAction(): G4UserRunAction() {

    // Create an analysis manager
    // in analysis.hh you can chose which one to use
    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
    G4cout << "Using" << analysisManager->GetType() << G4endl;

    // initialization of defaults
    analysisManager->SetVerboseLevel(1);
    analysisManager->SetFileName("muon_Hits");

    G4int n_bins = 100;
    G4double upper_time_limit = 10.*us;
    G4double lower_time_limit = 0.;

    analysisManager->CreateH1("el_dec1","e+/e- from decay SC1 time", n_bins ,
                              lower_time_limit, upper_time_limit); // h1 Id = 0
    analysisManager->CreateH1("el_ioni1","e- from ionization SC1 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 1
    analysisManager->CreateH1("el_bound1","e- from bound decay SC1 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 2
    analysisManager->CreateH1("el_cap1","e- from capture SC1 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 3
    analysisManager->CreateH1("prot1","protons SC1 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 4
    analysisManager->CreateH1("gamma1","gamma SC1 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 5
    analysisManager->CreateH1("el_dec2","e+/e- from decay SC2 time", n_bins ,
                              lower_time_limit, upper_time_limit); // h1 Id = 6
    analysisManager->CreateH1("el_ioni2","e- from ionization SC2 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 7
    analysisManager->CreateH1("el_bound2","e- from bound decay SC2 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 8
    analysisManager->CreateH1("el_cap2"," e- from capture SC2 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 9
    analysisManager->CreateH1("prot2","protons SC2 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 11
    analysisManager->CreateH1("gamma2","gamma SC2 time", n_bins,
                              lower_time_limit, upper_time_limit); // h1 Id = 12


    //Creating ntuple
    analysisManager->CreateNtuple("data", "Hits");
    analysisManager->CreateNtupleDColumn("Eventnumber");    // column Id = 0
    analysisManager->CreateNtupleDColumn("Time");  // column Id = 1
    analysisManager->CreateNtupleDColumn("DepositedEnergy"); // column Id = 2
    analysisManager->CreateNtupleDColumn("OriginalEnergy");    // column Id = 3
    analysisManager->CreateNtupleDColumn("DecayFlag");  //column Id = 4
    analysisManager->CreateNtupleDColumn("particleFlag"); //column Id = 5
    analysisManager->CreateNtupleDColumn("Origin(LogicalVolume)"); //column Id 6
    analysisManager->CreateNtupleDColumn("Detector"); // column Id = 7
    analysisManager->CreateNtupleDColumn("z-Momentum"); // column Id = 8
    analysisManager->CreateNtupleDColumn("Muon-relative Time"); // column Id = 9
    analysisManager->CreateNtupleDColumn("ParentID"); // column Id = 10
    analysisManager->FinishNtuple();
}
RunAction::~RunAction(){
    delete G4AnalysisManager::Instance();
}

void RunAction::BeginOfRunAction(const G4Run *) {
    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
    analysisManager->OpenFile();
}

void RunAction::EndOfRunAction(const G4Run *) {

    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
    analysisManager->Write();
    analysisManager->CloseFile();
}
