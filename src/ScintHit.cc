//
// Created by cgrubitz on 24.10.16.
//

#include "ScintHit.hh"

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

G4ThreadLocal G4Allocator<ScintHit>* ScintHitAllocator=0;

ScintHit::ScintHit(G4String name, G4double e, G4String org,
                   G4double eorg, G4String proc, G4int track, G4double momz)
        : G4VHit(), fId(name), fTime(0.0), fEnergy(e),
          fOrigin(org), fOrgEnergy(eorg), fProcess(proc),
          fTrack(track), fMomentum(momz)
{}

ScintHit::~ScintHit() {}

ScintHit::ScintHit(const ScintHit &right) : G4VHit() {
        fId = right.fId;
        fTime = right.fTime;
        fEnergy  = right.fEnergy;
        fPLogV = right.fPLogV;
        fOrigin = right.fOrigin;
        fOrgEnergy = right.fOrgEnergy;
        fProcess = right.fProcess;
        fTrack = right.fTrack;
        fMomentum = right.fMomentum;
}

const ScintHit& ScintHit::operator=(const ScintHit &right) {
    fId = right.fId;
    fTime = right.fTime;
    fEnergy = right.fEnergy;
    fPLogV = right.fPLogV;
    fOrigin = right.fOrigin;
    fOrgEnergy = right.fOrgEnergy;
    fProcess = right.fProcess;
    fTrack = right.fTrack;
    fMomentum = right.fMomentum;
    return *this;
}

int ScintHit::operator==(const ScintHit &/*right*/) const
{
    return 0;
}

const std::map<G4String,G4AttDef>* ScintHit::GetAttDefs() const
{
     G4bool isNew;
     std::map<G4String,G4AttDef>* store
     = G4AttDefStore::GetInstance("ScintHit",isNew);

     if (isNew) {
         (*store)["HitType"]
           = G4AttDef("HitType","Hit Type","Physics","","G4String");

         (*store)["ID"]
           = G4AttDef("ID","ID","Physics","","G4String");

         (*store)["Time"]
           = G4AttDef("Time","Time","Physics","G4BestUnit","G4double");

         (*store)["Energy"]
                 = G4AttDef("Energy","Energy","Physics","G4BestUnit","G4double");

         (*store)["LVol"]
                 = G4AttDef("LVol","Logical Volume","Physics","","G4String");

         (*store)["Origin"]
                 = G4AttDef("Origin", "Origin","Physics", "", "G4String");

         (*store)["OrigEnergy"]
                 = G4AttDef("OrigEnergy", "kinetic Energy at Origin","Physics",
                            "", "G4double");

         (*store)["Proc"]
                 = G4AttDef("Process", "created in Process","Physics" ,"", "G4String");
         (*store)["Track"]
                 = G4AttDef("TrackID", "number of Track", "Physics", "", "G4int");

         (*store)["Momentumz"]
                 = G4AttDef("Momentum", "Momentum Vector", "Physics", "", "G4double");

     }
     return store;
 }

std::vector<G4AttValue>* ScintHit::CreateAttValues() const
{
    std::vector<G4AttValue>* values = new std::vector<G4AttValue>;

    values->push_back(G4AttValue("HitType","ScintHit",""));
    values->push_back(G4AttValue("ID", fId ,""));
    values->push_back(G4AttValue("Time",G4BestUnit(fTime,"Time"),""));
    values->push_back(G4AttValue("Energy",G4BestUnit(fEnergy,"Energy"),""));

    if (fPLogV)
        values->push_back(G4AttValue("LVol",fPLogV->GetName(),""));
    else
        values->push_back(G4AttValue("LVol"," ",""));

    values->push_back(G4AttValue("Origin",fOrigin,""));
    values->push_back(G4AttValue("OrigEnergy",G4BestUnit(fOrgEnergy,"OrigEnergy"),""));
    values->push_back(G4AttValue("Process",fProcess,""));
    values->push_back(G4AttValue("TrackID", fTrack, ""));
    values->push_back(G4AttValue("Momentum", fMomentum, ""));

    return values;
}

void ScintHit::Print()
{
    G4cout << "particle " << fId<< "  " << fTime/ns << " (nsec) " << fEnergy
           << " MeV" << " came from volume " << fOrigin << " was created in "<<
           fProcess << "Tracknumber is " << fTrack << " Momentum "<< fMomentum <<G4endl;
}
