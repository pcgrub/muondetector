//
// Created by cgrubitz on 27.10.16.
//

#include "../include/RunAction.hh"

#include "Analysis.hh"

#include "Run.hh"
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

    analysisManager->CreateH1("Chamber1","Drift Chamber 1 # Hits", 50, 0., 7); // h1 Id = 0
    analysisManager->CreateH1("Chamber2","Drift Chamber 2 # Hits", 50, 0., 7); // h1 Id = 1


    //Creating ntuple
    analysisManager->CreateNtuple("data", "Hits");
    analysisManager->CreateNtupleDColumn("Eventnumber");    // column Id = 0
    analysisManager->CreateNtupleDColumn("Time");  // column Id = 1
    analysisManager->CreateNtupleDColumn("EnergySc1"); // column Id = 2
    analysisManager->CreateNtupleDColumn("OriginalEnergySc1");    // column Id = 3
    analysisManager->CreateNtupleDColumn("DecayFlagSc1");  //column Id = 4
    analysisManager->CreateNtupleDColumn("particleFlagSc1"); //column Id = 5
    analysisManager->CreateNtupleDColumn("Origin(Logical Volume)SC1Hit"); //column Id 6
    analysisManager->CreateNtupleDColumn("Detector"); // column Id = 7
    analysisManager->CreateNtupleDColumn("Angle at Vertex"); // column Id = 8
    analysisManager->FinishNtuple();
}
RunAction::~RunAction(){
    delete G4AnalysisManager::Instance();
}

void RunAction::BeginOfRunAction(const G4Run *) {
    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
    analysisManager->OpenFile();
}

void RunAction::EndOfRunAction(const G4Run * /*run*/) {

    G4AnalysisManager* analysisManager = G4AnalysisManager::Instance();
    analysisManager->Write();
    analysisManager->CloseFile();
}

G4Run* RunAction::GenerateRun() {
    return new Run;
}