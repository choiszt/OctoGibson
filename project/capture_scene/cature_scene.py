import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.asset_utils import get_available_g_scenes, get_available_og_scenes
from omnigibson.utils.ui_utils import choose_from_options,KeyboardRobotController
from omnigibson.sensors import VisionSensor
from collections import OrderedDict
from omnigibson import object_states
import numpy as np
import json,os
# Configure macros for maximum performance
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_FLATCACHE = True
gm.ENABLE_OBJECT_STATES = False
gm.ENABLE_TRANSITION_RULES = False
import time
from robot_action import *
"['Beechwood_0_int', 'Beechwood_1_int', 'Benevolence_0_int', 'Benevolence_1_int', 'Benevolence_2_int', 'Ihlen_0_int', 'Ihlen_1_int',"
"'Merom_0_int', 'Merom_1_int', 'Pomaria_0_int', 'Pomaria_1_int', 'Pomaria_2_int', 'Rs_int', 'Wainscott_0_int', 'Wainscott_1_int']"
def main(random_selection=False, headless=False, short_exec=False):
    scenename="Wainscott_1_int"
    print(f"load:{scenename}")
    scene_cfg = dict(type="InteractiveTraversableScene",
                    scene_model=scenename,
                    not_load_object_categories=["ceilings"])
    robot0_cfg = dict(
        type="Fetch",
        obs_modalities=["rgb","depth","normal","seg_instance"],     # we're just doing a grasping demo so we don't need all observation modalities
        action_type="continuous",
        action_normalize=True,
        visible=False
    )    
    cfg=dict(scene=scene_cfg,robots=[robot0_cfg])    
    env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)
    robot = env.robots[0]

    
    action_generator = KeyboardRobotController(robot=robot)
    for sensor in robot.sensors.values():
        if isinstance(sensor, VisionSensor):
            sensor.image_height = 720
            sensor.image_width = 720
    # Print out relevant keyboard info if using keyboard teleop
    action_generator.print_keyboard_teleop_info()   
    action=np.zeros(11)
    og.sim.viewer_camera.set_position_orientation(
        position=np.array([0,  0,  19]),
        orientation=np.array([ 0,0,0,0]),
    )
    camera= og.sim.viewer_camera 
    def donothing(navi):
        dumbact=OrderedDict([('robot0', navi)])
        step=0
        for _ in range(5):
            # og.sim.step()
            env.step(dumbact)
            step += 1
    donothing(action)
    camera.set_position_orientation(position=np.array([0,  0,  19]),orientation=np.array([ 0,0,0,0]),)

    donothing(action)
    print("start capturing...")
    FlyingCapture(camera,scenename)
    donothing(action)
        


if __name__ == "__main__":
    main()
