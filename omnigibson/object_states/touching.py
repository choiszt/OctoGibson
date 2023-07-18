from omnigibson.object_states.contact_bodies import ContactBodies
from omnigibson.object_states.kinematics import KinematicsMixin
from omnigibson.object_states.object_state_base import BooleanState, RelativeObjectState
from omnigibson.utils.constants import PrimType

class Touching(KinematicsMixin, RelativeObjectState, BooleanState):
    def _set_value(self, other, new_value):
        raise NotImplementedError()

    @staticmethod
    def _check_contact(obj_a, obj_b):
        return len(set(obj_a.links.values()) & obj_b.states[ContactBodies].get_value()) > 0

    def _get_value(self, other):
        if self.obj.prim_type == PrimType.CLOTH and other.prim_type == PrimType.CLOTH:
            raise ValueError("Cannot detect contact between two cloth objects.")
        # If one of the objects is the cloth object, the contact will be asymmetrical.
        # The rigid object will appear in the ContactBodies of the cloth object, but not the other way around.
        elif self.obj.prim_type == PrimType.CLOTH:
            return self._check_contact(other, self.obj)
        elif other.prim_type == PrimType.CLOTH:
            return self._check_contact(self.obj, other)
        else:
            return self._check_contact(other, self.obj) and self._check_contact(self.obj, other)
