//
// Created by cgrubitz on 19.10.16.
//

#ifndef SLACTUT_MYON_PRIM_GEN_ACTION_HH
#define SLACTUT_MYON_PRIM_GEN_ACTION_HH

#endif //SLACTUT_MYON_PRIM_GEN_ACTION_HH

#include <G4GeneralParticleSource.hh>
#include "G4VUserPrimaryGeneratorAction.hh"
#include "globals.hh"
#include "G4ParticleGun.hh"

class G4ParticleGun;
class G4GenericMessenger;
class G4Event;
class G4ParticleDefinition;

class MyonPrimaryGeneratorAction: public G4VUserPrimaryGeneratorAction {
public:
    MyonPrimaryGeneratorAction();
    virtual ~MyonPrimaryGeneratorAction();

    virtual void GeneratePrimaries(G4Event*);

private:
    void DefineCommands();

    G4GeneralParticleSource* fParticleGun;
    G4GenericMessenger* fMessenger;
    G4ParticleDefinition* fMuon;
    G4ParticleDefinition* fAMuon;
};
