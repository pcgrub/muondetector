//
// Created by cgrubitz on 27.10.16.
//

#include "../include/CopperHit.hh"

#include "G4VVisManager.hh"
#include "G4VisAttributes.hh"
#include "G4Circle.hh"
#include "G4Colour.hh"
#include "G4AttDefStore.hh"
#include "G4AttDef.hh"
#include "G4AttValue.hh"
#include "G4UIcommand.hh"
#include "G4UnitsTable.hh"
#include "G4SystemOfUnits.hh"
#include "G4ios.hh"

CopperHit::CopperHit(G4int i,G4double t, G4double e)
        : G4VHit(), fId(i), fTime(t), fEnergy(e)
{}

void CopperHit::Print()
{
    G4cout << " Scint[" << fId << "] " << fTime/ns << " (nsec)" << fEnergy
           << "MeV" <<G4endl;
}
