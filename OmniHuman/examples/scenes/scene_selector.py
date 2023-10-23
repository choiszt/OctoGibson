import omnigibson as og
from omnigibson.macros import gm
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

    cfg = {
        "scene": {
            "type": "InteractiveTraversableScene",
            "scene_model": "Rs_int",
        },
        "robots": [
            # {
            #     "type": "Turtlebot",
            #     "obs_modalities": ["scan", "rgb", "depth"],
            #     "action_type": "continuous",
            #     "action_normalize": True,
            # },
                            {
        "type": "Turtlebot", 
        "name": "choiszt", 
        "visual_only":False,
        "usd_path": f"/home/liushuai/Desktop/animation/Actorcore-Omniverse-1023-455651/Actor/party-m-0001/party-m-0001.usd",
        "scale":0.01,
                        "obs_modalities": ["scan", "rgb", "depth"],
                "action_type": "continuous",
                "action_normalize": True,
        }
        ],
    }

    # If the scene type is interactive, also check if we want to quick load or full load the scene
    cfg["scene"]["load_object_categories"] = ["floors", "walls", "ceilings"]

    # Load the environment
    env = og.Environment(configs=cfg)
    ag.get_character("/World/choiszt")
    # Allow user to move camera more easily
    if not gm.HEADLESS:
        og.sim.enable_viewer_camera_teleoperation()

    # Run a simple loop and reset periodically
    max_iterations = 10 if not short_exec else 1
    while True:
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)

    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()
