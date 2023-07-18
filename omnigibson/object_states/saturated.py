import numpy as np
from omnigibson.macros import create_module_macros
from omnigibson.object_states.object_state_base import RelativeObjectState, BooleanState
from omnigibson.object_states.particle_modifier import ParticleRemover
from omnigibson.utils.python_utils import assert_valid_key


# Create settings for this module
m = create_module_macros(module_path=__file__)


class Saturated(RelativeObjectState, BooleanState):
    def _get_value(self, system):
        return self.obj.states[ParticleRemover].check_at_limit(system=system)

    def _set_value(self, system, new_value):
        assert_valid_key(key=system, valid_keys=ParticleRemover.supported_active_systems, name="particle system")
        # Only set the value if it's different than what currently exists
        if new_value != self.get_value(system):
            self.obj.states[ParticleRemover].set_at_limit(system, new_value)
        return True

    def get_texture_change_params(self):
        colors = []

        for system in ParticleRemover.supported_active_systems:
            if self.get_value(system):
                colors.append(system.color)

        if len(colors) == 0:
            # If no fluid system has Soaked=True, keep the default albedo value
            albedo_add = 0.0
            diffuse_tint = [1.0, 1.0, 1.0]
        else:
            albedo_add = 0.1
            avg_color = np.mean(colors, axis=0)
            # Add a tint of avg_color
            # We want diffuse_tint to sum to 2.5 to result in the final RGB to sum to 1.5 on average
            # This is because an average RGB color sum to 1.5 (i.e. [0.5, 0.5, 0.5])
            # (0.5 [original avg RGB per channel] + 0.1 [albedo_add]) * 2.5 = 1.5
            diffuse_tint = np.array([0.5, 0.5, 0.5]) + avg_color / np.sum(avg_color)
            diffuse_tint = diffuse_tint.tolist()

        return albedo_add, diffuse_tint

    @staticmethod
    def get_dependencies():
        return RelativeObjectState.get_dependencies() + [ParticleRemover]
