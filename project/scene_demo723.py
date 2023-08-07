import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.asset_utils import get_available_g_scenes, get_available_og_scenes
from omnigibson.utils.ui_utils import choose_from_options,KeyboardRobotController

# Configure macros for maximum performance
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_FLATCACHE = True
gm.ENABLE_OBJECT_STATES = False
gm.ENABLE_TRANSITION_RULES = False


def main(random_selection=False, headless=False, short_exec=False):
    """
    Prompts the user to select any available interactive scene and loads a turtlebot into it.
    It steps the environment 100 times with random actions sampled from the action space,
    using the Gym interface, resetting it 10 times.
    """
    og.log.info(f"Demo {__file__}\n    " + "*" * 80 + "\n    Description:\n" + main.__doc__ + "*" * 80)

    # Choose the scene type to load
    # scene_options = {
    #     "InteractiveTraversableScene": "Procedurally generated scene with fully interactive objects",
    #     # "StaticTraversableScene": "Monolithic scene mesh with no interactive objects",
    # }
    # scene_type = choose_from_options(options=scene_options, name="scene type", random_selection=random_selection)

    # # Choose the scene model to load
    # scenes = get_available_og_scenes() if scene_type == "InteractiveTraversableScene" else get_available_g_scenes()
    # scene_model = choose_from_options(options=scenes, name="scene model", random_selection=random_selection)

    cfg = {
        "scene": {
            "type": "InteractiveTraversableScene",
            "scene_model": "choiszt"
        },
        "robots": [
            {
                "type": "Turtlebot",
                "obs_modalities": ["scan", "rgb", "depth"],
                "action_type": "continuous",
                "action_normalize": True,
                "scale":1.5
            },
        ],
    }

    # If the scene type is interactive, also check if we want to quick load or full load the scene

    # Load the environment
    env = og.Environment(configs=cfg)
    robot = env.robots[0]
    robot.set_position([-1.33887291 ,4.79978561 ,0.01504258])
    action_generator = KeyboardRobotController(robot=robot)

    # Print out relevant keyboard info if using keyboard teleop
    action_generator.print_keyboard_teleop_info()    
    
    # Allow user to move camera more easily
    from collections import OrderedDict
    import numpy as np
    dumbact=OrderedDict([('robot0', np.zeros(2))])
    dumbact=action_generator.get_teleop_action()
    if not gm.HEADLESS:
        og.sim.enable_viewer_camera_teleoperation()
    step=0
    # Run a simple loop and reset periodically
    max_iterations = 10 if not short_exec else 1
    for j in range(max_iterations):
        # og.log.info("Resetting environment")
        # env.reset()
        for i in range(1000):
            action = env.action_space.sample()
            state, reward, done, info = env.step(dumbact)
            for _ in range(1000):
                state, reward, done, info = env.step(dumbact)
                # step+=1
            print(robot.get_position())
            if done:
                og.log.info("Episode finished after {} timesteps".format(i + 1))
                break

    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()
