//
// Created by cgrubitz on 27.10.16.
//

#ifndef MUONDETECTOR_COPPERHIT_HH_HH
#define MUONDETECTOR_COPPERHIT_HH_HH

#include "G4VHit.hh"
#include "G4THitsCollection.hh"
#include "G4Allocator.hh"
#include "G4ThreeVector.hh"
#include "G4LogicalVolume.hh"
#include "G4Transform3D.hh"
#include "G4RotationMatrix.hh"

class G4AttDef;
class G4AttValue;

class CopperHit :public G4VHit{

public:
    CopperHit(G4int i, G4double t, G4double e);
    virtual ~CopperHit() {}

    void Print();

    G4int GetID() const {return fId;}
    void SetTime(G4double val) { fTime = val; }
    G4double GetTime() const { return fTime; }
    G4double GetEnergy() const {return fEnergy;}

private:
    G4int fId;
    G4double fTime;
    G4double fEnergy;
};

typedef G4THitsCollection<CopperHit> CopperHitsCollection;

extern G4ThreadLocal G4Allocator<CopperHit>* CopperHitAllocator;


#endif //MUONDETECTOR_COPPERHIT_HH_HH
