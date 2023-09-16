import os
import json
import yaml
import argparse
import time

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options

gm.ENABLE_OBJECT_STATES = True
gm.USE_GPU_DYNAMICS = True

def main(idx, random_selection=False, headless=False, short_exec=False):

    config_filename = "./bddl_demo.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
    cfg["task"]["online_object_sampling"] = False

    with open('task_scene.json') as f:
        data = json.load(f)

    data_list = list(data.items())
    data_entry = data_list[idx]

    og.log.info(f'data_entry_{data_entry}')

    cfg["scene"]["scene_model"] = data_entry[1]
    cfg["task"]["activity_name"] = data_entry[0]

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

    time.sleep(5)
    print('successful loading')
    og.log.info('successful loading')
    create_success_file(idx, data_entry)
    og.log.info('successful creation')

   
    env.close()


def create_success_file(idx, data_entry):
    success_directory = 'success_0829'
    
    if not os.path.exists(success_directory):
        os.makedirs(success_directory)
    
    success_filename = f"{idx}_{data_entry[0]}__{data_entry[1]}.txt"
    success_filepath = os.path.join(success_directory, success_filename)
    
    # Creating an empty file
    open(success_filepath, 'w').close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set the index for data entry.')
    parser.add_argument('idx', type=int, help='Index for data entry')
    args = parser.parse_args()
    
    main(idx=args.idx)
