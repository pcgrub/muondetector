//
// Created by piet on 03.11.16.
//

#ifndef MUONDETECTOR_RUN_H
#define MUONDETECTOR_RUN_H

#include "G4Run.hh"

class G4Event;

class Run : public G4Run {
public:
    Run();
    virtual ~Run() {};

    virtual void Merge(const G4Run*);
};

#endif //MUONDETECTOR_RUN_H
