//
// Created by cgrubitz on 20.10.16.
//

#include "../include/MuonActionInitialization.hh"
#include "../include/MuonPrimaryGeneratorAction.hh"
#include "../include/RunAction.hh"
#include "../include/EventAction.hh"
#include "../include/SteppingAction.hh"

MuonActionInitialization::MuonActionInitialization()
        :G4VUserActionInitialization() { }

MuonActionInitialization::~MuonActionInitialization() {}

void MuonActionInitialization::BuildForMaster() const {

    // called by the master thread. when merging of thread results
    // is needed one should create an instance of Rn action here
    SetUserAction(new RunAction);
}

void MuonActionInitialization::Build() const {

    //This is called by each worker thread.
    //Create here the user-actions needed by each thread:
    // RunAction, EventAction, SteppingAction, StackingAction

    SetUserAction(new MyonPrimaryGeneratorAction);
    SetUserAction(new RunAction);
    EventAction* event = new EventAction();
    SetUserAction(event);
    SetUserAction(new SteppingAction(event));
}
