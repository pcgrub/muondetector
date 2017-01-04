//
// Created by cgrubitz on 24.10.16.
//

#ifndef MUONDETECTOR_SCINTHIT_HH
#define MUONDETECTOR_SCINTHIT_HH

#include "G4VHit.hh"
#include "G4THitsCollection.hh"
#include "G4Allocator.hh"
#include "G4ThreeVector.hh"
#include "G4LogicalVolume.hh"
#include "G4Transform3D.hh"
#include "G4RotationMatrix.hh"

class G4AttDef;
class G4AttValue;

class ScintHit :public G4VHit{

public:
    ScintHit(G4String name, G4double e, G4String org, G4double eorg, G4String proc, G4int track,
    G4double momz);
    ScintHit(const ScintHit &right);
    virtual ~ScintHit();

    const ScintHit& operator=(const ScintHit &right);
    int operator==(const ScintHit &right) const;

    virtual const std::map<G4String,G4AttDef>* GetAttDefs() const;
    virtual std::vector<G4AttValue>* CreateAttValues() const;


    void Print();
    G4String GetName() const {return fId;}

    void SetTime(G4double val) { fTime = val; }
    G4double GetTime() const { return fTime; }

    G4double GetEnergy() const {return fEnergy;}

    G4String GetOrigin() const { return fOrigin;}

    G4double GetOriginalKineticEnergy() const {return fOrgEnergy;}

    G4String GetProcess() const {return fProcess;}

    G4int GetTrack() const { return fTrack;}

    G4double GetMomentum() const {return fMomentum;}

private:
    G4String fId;
    G4double fTime;
    G4double fEnergy;
    G4String fOrigin;
    G4double fOrgEnergy;
    G4String fProcess;
    G4int fTrack;
    G4double fMomentum;

};

typedef G4THitsCollection<ScintHit> ScintHitsCollection;

extern G4ThreadLocal G4Allocator<ScintHit>* ScintHitAllocator;

#endif //MUONDETECTOR_SCINTHIT_HH
