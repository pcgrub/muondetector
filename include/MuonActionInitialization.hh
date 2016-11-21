//
// Created by cgrubitz on 20.10.16.
//

#ifndef SLACTUT_ACTION_INIT_HH
#define SLACTUT_ACTION_INIT_HH

#include "G4VUserActionInitialization.hh"

// Action init class

class MuonActionInitialization : public G4VUserActionInitialization {
public:
    MuonActionInitialization();
    virtual  ~MuonActionInitialization();

    virtual void BuildForMaster() const;

    virtual void Build() const;
};

#endif //SLACTUT_ACTION_INIT_HH