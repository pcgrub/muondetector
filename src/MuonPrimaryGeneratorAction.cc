//
// Created by cgrubitz on 19.10.16.
//

#include "MuonPrimaryGeneratorAction.hh"

#include "G4Event.hh"
#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4GenericMessenger.hh"
#include "G4SystemOfUnits.hh"
#include "Randomize.hh"
#include "G4Decay.hh"

MyonPrimaryGeneratorAction::MyonPrimaryGeneratorAction()
        : G4VUserPrimaryGeneratorAction(),
          fParticleGun(0), fMessenger(0),
          fMuon (0), fAMuon(0)
{
    // initialize particle gun with number of particles
    // later it will be replaced by GPS
    //G4int n_particle = 1;
    fParticleGun = new G4GeneralParticleSource(/*n_particle*/);

    // where particles are looked up
    G4ParticleTable* particleTable = G4ParticleTable::GetParticleTable();

    // get particle info form the table
    G4String particleName;
    fMuon = particleTable->FindParticle(particleName="mu-");
    fMuon->SetPDGStable(false);

    fAMuon = particleTable->FindParticle(particleName="mu+");
    fAMuon->SetPDGStable(false);
    // default particle kinematics
    //fParticleGun->SetParticlePosition(G4ThreeVector(0.,0.,-2.*m));
    fParticleGun->SetParticleDefinition(fMuon);
    // define commands for this class
    DefineCommands();
}

MyonPrimaryGeneratorAction::~MyonPrimaryGeneratorAction() {
    // mandatory deletion
    delete fParticleGun;
    delete fMessenger;

}

void MyonPrimaryGeneratorAction::GeneratePrimaries(G4Event* event) {
    G4ParticleDefinition* particle;
    // this is the part of the program where the properties of the
    // beam particles are set. They are:

    G4int i = (int(2.25*G4UniformRand()));
    if (i==0){particle=fMuon;}
    else {particle=fAMuon;}
    fParticleGun->SetParticleDefinition(particle);
    particle->SetPDGStable(false);

    // adds s the particle gun tu the event
    // an event is created automatically and deleted
    // automatically by G4RunManager
    fParticleGun->GeneratePrimaryVertex(event);

}

void MyonPrimaryGeneratorAction::DefineCommands(){}
