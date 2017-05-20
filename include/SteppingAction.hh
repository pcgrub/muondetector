//
// Created by piet on 27.04.17.
//

#ifndef MUONDETECTOR_TRACKINGACTION_HH
#define MUONDETECTOR_TRACKINGACTION_HH



#include "G4UserSteppingAction.hh"

class EventAction;

class SteppingAction : public G4UserSteppingAction {
    public:
        SteppingAction(EventAction*);
        ~SteppingAction() {};

        virtual void UserSteppingAction(const G4Step*);

    private:
        EventAction* fEventAction;
};

#endif //MUONDETECTOR_TRACKINGACTION_HH