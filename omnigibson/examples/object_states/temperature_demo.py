import numpy as np

import omnigibson as og
from omnigibson import object_states
from omnigibson.macros import gm

# Make sure object states are enabled
gm.ENABLE_OBJECT_STATES = True


def main(random_selection=False, headless=False, short_exec=False):
    """
    Demo of temperature change
    Loads a stove, a microwave and an oven, all toggled on, and five frozen apples
    The user can move the apples to see them change from frozen, to normal temperature, to cooked and burnt
    This demo also shows how to load objects ToggledOn and how to set the initial temperature of an object
    """
    og.log.info(f"Demo {__file__}\n    " + "*" * 80 + "\n    Description:\n" + main.__doc__ + "*" * 80)

    # Define specific objects we want to load in with the scene directly
    obj_configs = []

    # Light
    obj_configs.append(dict(
        type="LightObject",
        light_type="Sphere",
        name="light",
        radius=0.01,
        intensity=1e8,
        position=[-2.0, -2.0, 1.0],
    ))

    # Stove
    obj_configs.append(dict(
        type="DatasetObject",
        name="stove",
        category="stove",
        model="yhjzwg",
        position=[0, 0, 0.69],
    ))

    # Microwave
    obj_configs.append(dict(
        type="DatasetObject",
        name="microwave",
        category="microwave",
        model="hjjxmi",
        scale=0.25,
        position=[2.5, 0, 0.10],
    ))

    # Oven
    obj_configs.append(dict(
        type="DatasetObject",
        name="oven",
        category="oven",
        model="wuinhm",
        position=[-1.25, 0, 0.88],
    ))

    # Tray
    obj_configs.append(dict(
        type="DatasetObject",
        name="tray",
        category="tray",
        model="xzcnjq",
        scale=0.15,
        position=[-0.25, -0.12, 1.26],
    ))

    # Fridge
    obj_configs.append(dict(
        type="DatasetObject",
        name="fridge",
        category="fridge",
        model="hivvdf",
        abilities={
            "coldSource": {
                "temperature": -100.0,
                "requires_inside": True,
            }
        },
        position=[1.25, 0, 0.81],
    ))

    # 5 Apples
    for i in range(5):
        obj_configs.append(dict(
            type="DatasetObject",
            name=f"apple{i}",
            category="apple",
            model="agveuv",
            position=[0, i * 0.1, 5.0],
        ))

    # Create the scene config to load -- empty scene with desired objects
    cfg = {
        "scene": {
            "type": "Scene",
        },
        "objects": obj_configs,
    }

    # Create the environment
    env = og.Environment(configs=cfg, action_timestep=1 / 60., physics_timestep=1 / 60.)

    # Get reference to relevant objects
    stove = env.scene.object_registry("name", "stove")
    microwave = env.scene.object_registry("name", "microwave")
    oven = env.scene.object_registry("name", "oven")
    tray = env.scene.object_registry("name", "tray")
    fridge = env.scene.object_registry("name", "fridge")
    apples = list(env.scene.object_registry("category", "apple"))

    # Set camera to appropriate viewing pose
    og.sim.viewer_camera.set_position_orientation(
        position=np.array([ 0.46938863, -3.97887141,  1.64106008]),
        orientation=np.array([0.63311689, 0.00127259, 0.00155577, 0.77405359]),
    )

    # Let objects settle
    for _ in range(25):
        env.step(np.array([]))

    # Turn on all scene objects
    stove.states[object_states.ToggledOn].set_value(True)
    microwave.states[object_states.ToggledOn].set_value(True)
    oven.states[object_states.ToggledOn].set_value(True)

    # Set initial temperature of the apples to -50 degrees Celsius, and move the apples to different objects
    for apple in apples:
        apple.states[object_states.Temperature].set_value(-50)
    apples[0].states[object_states.Inside].set_value(oven, True)
    apples[1].set_position(stove.states[object_states.HeatSourceOrSink].link.get_position() + np.array([0, 0, 0.1]))
    apples[2].states[object_states.OnTop].set_value(tray, True)
    apples[3].states[object_states.Inside].set_value(fridge, True)
    apples[4].states[object_states.Inside].set_value(microwave, True)

    steps = 0
    max_steps = -1 if not short_exec else 1000

    # Main recording loop
    locations = [f'{loc:>20}' for loc in ["Inside oven", "On stove", "On tray", "Inside fridge", "Inside microwave"]]
    print()
    print(f"{'Apple location:':<20}", *locations)
    while steps != max_steps:
        env.step(np.array([]))
        temps = [f"{apple.states[object_states.Temperature].get_value():>20.2f}" for apple in apples]
        print(f"{'Apple temperature:':<20}", *temps, end="\r")
        steps += 1

    # Always close env at the end
    env.close()


if __name__ == "__main__":
    main()
