import os
import json
import yaml

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options

# Make sure object states are enabled
gm.ENABLE_OBJECT_STATES = True


def main(random_selection=False, headless=False, short_exec=False):

    failure = {}

    config_filename="/shared/liushuai/OmniGibson/project/bddl_demo.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
    cfg["task"]["online_object_sampling"] = False

    with open('task_scene.json') as f:
        data = json.load(f)
    for k, v in data.items():
        cfg["scene"]["scene_mdoel"] = v
        cfg["task"]["activity_name"] = k

        try:
            # Load the environment
            env = og.Environment(configs=cfg)

            # Allow user to move camera more easily
            og.sim.enable_viewer_camera_teleoperation()

            # Run a simple loop and reset periodically
            max_iterations = 1 if not short_exec else 1
            for j in range(max_iterations):
                og.log.info("Resetting environment")
                env.reset()
                for i in range(30):
                    action = env.action_space.sample()
                    state, reward, done, info = env.step(action)
                    if done:
                        og.log.info("Episode finished after {} timesteps".format(i + 1))
                        break

            # Always close the environment at the end
            env.close()
        except:
            failure[k] = v
    
    with open('fail.json', 'w') as f:
        f.write(json.dumps(failure, indent=4))


if __name__ == "__main__":
    main()
