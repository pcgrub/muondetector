//
// Created by piet on 14.11.16.
//

#ifndef MUONDETECTOR_TESTEVENTACTION_HH
#define MUONDETECTOR_TESTEVENTACTION_HH

#endif //MUONDETECTOR_TESTEVENTACTION_HH
#include "G4UserEventAction.hh"
#include "globals.hh"


class TestEventAction :public G4UserEventAction{
public:
    TestEventAction();
    virtual ~TestEventAction();

    virtual void BeginOfEventAction(const G4Event*);
    virtual void EndOfEventAction(const G4Event*);

private:
    G4int fSCID1;

};
