from omnigibson.object_states.object_state_base import BooleanStateMixin, AbsoluteObjectState

class Inventory(AbsoluteObjectState, BooleanStateMixin):
    def __init__(self, obj):
        super().__init__(obj)
        self.inv = False
    
    def _get_value(self):
        return self.inv
    
    def _set_value(self, new_value):
        self.inv = new_value