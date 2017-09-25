//
// Created by cgrubitz on 27.10.16.
//

#ifndef MUONDETECTOR_RUNACTION_HH
#define MUONDETECTOR_RUNACTION_HH

#include "G4UserRunAction.hh"
#include "globals.hh"

class G4Run;

class RunAction : public G4UserRunAction {
public:
    RunAction();
    virtual ~RunAction();

    virtual void BeginOfRunAction(const G4Run*);
    virtual void EndOfRunAction(const G4Run*);
};

#endif //MUONDETECTOR_RUNACTION_HH
