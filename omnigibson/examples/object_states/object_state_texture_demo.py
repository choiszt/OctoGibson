import numpy as np
import omnigibson as og
from omnigibson import object_states
from omnigibson.macros import gm, macros
from omnigibson.systems import get_system
from omnigibson.utils.constants import ParticleModifyMethod

# Make sure object states are enabled, we're using GPU dynamics, and HQ rendering is enabled
gm.ENABLE_OBJECT_STATES = True
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_HQ_RENDERING = True


def main():
    # Create the scene config to load -- empty scene plus a light and a cabinet
    cfg = {
        "scene": {
            "type": "Scene",
            "floor_plane_visible": True,
        },
        "objects": [
            {
                "type": "LightObject",
                "name": "light",
                "light_type": "Sphere",
                "radius": 0.01,
                "intensity": 1e8,
                "position": [-2.0, -2.0, 1.0],
            },
            {
                "type": "DatasetObject",
                "name": "cabinet",
                "category": "bottom_cabinet",
                "model": "zuwvdo",
                "abilities": {
                    "freezable": {},
                    "cookable": {},
                    "burnable": {},
                    "saturable": {},
                    "toggleable": {},
                    "particleRemover": {
                        "method": ParticleModifyMethod.ADJACENCY,
                        "conditions": {
                            # For a specific particle system, this specifies what conditions are required in order for the
                            # particle applier / remover to apply / remover particles associated with that system
                            # The list should contain functions with signature condition() --> bool,
                            # where True means the condition is satisfied
                            # In this case, we only allow our cabinet to absorb water, with no conditions needed.
                            # This is needed for the Saturated ("saturable") state so that we can modify the texture
                            # according to the water.
                            # NOTE: This will only change color if gm.ENABLE_HQ_RENDERING and gm.USE_GPU_DYNAMICS is
                            # enabled!
                            "water": [],
                        },
            },
                },
                "position": [0, 0, 0.59],
            },
        ],
    }

    # Create the environment
    env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)

    # Set camera to appropriate viewing pose
    og.sim.viewer_camera.set_position_orientation(
        position=np.array([ 1.7789 , -1.68822,  1.13551]),
        orientation=np.array([0.57065614, 0.20331904, 0.267029  , 0.74947212]),
    )

    # Grab reference to object of interest
    obj = env.scene.object_registry("name", "cabinet")

    # Make sure all the appropriate states are in the object
    assert object_states.Frozen in obj.states
    assert object_states.Cooked in obj.states
    assert object_states.Burnt in obj.states
    assert object_states.Saturated in obj.states
    assert object_states.ToggledOn in obj.states

    def report_states():
        # Make sure states are propagated before printing
        for i in range(5):
            env.step(np.array([]))

        print("=" * 20)
        print("temperature:", obj.states[object_states.Temperature].get_value())
        print("obj is frozen:", obj.states[object_states.Frozen].get_value())
        print("obj is cooked:", obj.states[object_states.Cooked].get_value())
        print("obj is burnt:", obj.states[object_states.Burnt].get_value())
        print("obj is soaked:", obj.states[object_states.Saturated].get_value(get_system("water")))
        print("obj is toggledon:", obj.states[object_states.ToggledOn].get_value())
        print("obj textures:", obj.get_textures())

    # Report default states
    print("==== Initial state ====")
    report_states()

    # Notify user that we're about to freeze the object, and then freeze the object
    input("\nObject will be frozen. Press ENTER to continue.")
    obj.states[object_states.Temperature].set_value(-50)
    report_states()

    # Notify user that we're about to cook the object, and then cook the object
    input("\nObject will be cooked. Press ENTER to continue.")
    obj.states[object_states.Temperature].set_value(100)
    report_states()

    # Notify user that we're about to burn the object, and then burn the object
    input("\nObject will be burned. Press ENTER to continue.")
    obj.states[object_states.Temperature].set_value(250)
    report_states()

    # Notify user that we're about to reset the object to its default state, and then reset state
    input("\nObject will be reset to default state. Press ENTER to continue.")
    obj.states[object_states.Temperature].set_value(macros.object_states.temperature.DEFAULT_TEMPERATURE)
    obj.states[object_states.MaxTemperature].set_value(macros.object_states.temperature.DEFAULT_TEMPERATURE)
    report_states()

    # Notify user that we're about to soak the object, and then soak the object
    input("\nObject will be saturated with water. Press ENTER to continue.")
    obj.states[object_states.Saturated].set_value(get_system("water"), True)
    report_states()

    # Notify user that we're about to unsoak the object, and then unsoak the object
    input("\nObject will be unsaturated with water. Press ENTER to continue.")
    obj.states[object_states.Saturated].set_value(get_system("water"), False)
    report_states()

    # Notify user that we're about to toggle on the object, and then toggle on the object
    input("\nObject will be toggled on. Press ENTER to continue.")
    obj.states[object_states.ToggledOn].set_value(True)
    report_states()

    # Notify user that we're about to toggle off the object, and then toggle off the object
    input("\nObject will be toggled off. Press ENTER to continue.")
    obj.states[object_states.ToggledOn].set_value(False)
    report_states()

    # Close environment at the end
    input("Demo completed. Press ENTER to shutdown environment.")
    env.close()


if __name__ == "__main__":
    main()