import numpy as np

from omnigibson.macros import create_module_macros
from omnigibson.object_states.object_state_base import AbsoluteObjectState, BooleanState
from omnigibson.object_states.temperature import Temperature


# Create settings for this module
m = create_module_macros(module_path=__file__)

m.DEFAULT_HEAT_TEMPERATURE = 40

# When an object is set as heated, we will sample it between
# the heat temperature and these offsets.
m.HEATED_SAMPLING_RANGE_MIN = 10.0
m.HEATED_SAMPLING_RANGE_MAX = 20.0


class Heated(AbsoluteObjectState, BooleanState):
    def __init__(self, obj, heat_temperature=m.DEFAULT_HEAT_TEMPERATURE):
        super(Heated, self).__init__(obj)
        self.heat_temperature = heat_temperature

    @staticmethod
    def get_dependencies():
        return AbsoluteObjectState.get_dependencies() + [Temperature]

    def _set_value(self, new_value):
        if new_value:
            temperature = np.random.uniform(
                self.heat_temperature + m.HEATED_SAMPLING_RANGE_MIN,
                self.heat_temperature + m.HEATED_SAMPLING_RANGE_MAX,
            )
            return self.obj.states[Temperature].set_value(temperature)
        else:
            # We'll set the temperature just one degree below heating.
            return self.obj.states[Temperature].set_value(self.heat_temperature - 1.0)

    def _get_value(self):
        return self.obj.states[Temperature].get_value() >= self.heat_temperature

    # Nothing needs to be done to save/load Heated since it will happen due to temperature caching.
