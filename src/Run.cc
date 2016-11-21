//
// Created by piet on 03.11.16.
//

#include "../include/Run.hh"

#include "G4Event.hh"
#include "G4SDManager.hh"

Run::Run() : G4Run() {}

//Run::~Run(){}

void Run::Merge(const G4Run* aRun) {
    const Run* localRun = static_cast<const Run*>(aRun);
    G4Run::Merge(localRun);
}