import numpy as np

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.sensors import VisionSensor
from omnigibson.utils.ui_utils import choose_from_options, KeyboardRobotController
from omni_base.prompt_files.robot_action import *
GRASPING_MODES = dict(
    sticky="Sticky Mitten - Objects are magnetized when they touch the fingers and a CLOSE command is given",
    physical="Physical Grasping - No additional grasping assistance applied",
)

# Don't use GPU dynamics and Use flatcache for performance boost
gm.USE_GPU_DYNAMICS = False
gm.ENABLE_FLATCACHE = True


def main(random_selection=False, headless=False, short_exec=False):
    """
    Robot grasping mode demo with selection
    Queries the user to select a type of grasping mode
    """
    og.log.info(f"Demo {__file__}\n    " + "*" * 80 + "\n    Description:\n" + main.__doc__ + "*" * 80)

    # Choose type of grasping
    grasping_mode = choose_from_options(options=GRASPING_MODES, name="grasping mode", random_selection=random_selection)

    # Create environment configuration to use
    scene_cfg = dict(type="Scene")
    robot0_cfg = dict(
        type="Fetch",
        obs_modalities=["rgb","depth","normal","seg_instance"],     # we're just doing a grasping demo so we don't need all observation modalities
        action_type="continuous",
        action_normalize=True,
        grasping_mode=grasping_mode,
    )

    # Define objects to load
    table_cfg = dict(
        type="DatasetObject",
        name="table",
        category="breakfast_table",
        model="lcsizg",
        bounding_box=[0.5, 0.5, 0.8],
        fit_avg_dim_volume=False,
        fixed_base=True,
        position=[0.7, -0.1, 0.6],
        orientation=[0, 0, 0.707, 0.707],
    )

    chair_cfg = dict(
        type="DatasetObject",
        name="chair",
        category="straight_chair",
        model="amgwaw",
        bounding_box=None,
        fit_avg_dim_volume=True,
        fixed_base=False,
        position=[0.45, 0.65, 0.425],
        orientation=[0, 0, -0.9990215, -0.0442276],
    )

    box_cfg = dict(
        type="PrimitiveObject",
        name="box",
        primitive_type="Cube",
        rgba=[1.0, 0, 0, 1.0],
        size=0.05,
        position=[0.53, -0.1, 0.97],
    )
    pork_cfg=dict(
        type="DatasetObject",
        name="pork_ihekpm_0",
        category="pork",
        model="ihekpm",
        scale=0.15,
        position= [0.45, 0.65, 0.5],
        orientation= [0, 0, 0, 1.0],
    )
    # Compile config
    cfg = dict(scene=scene_cfg, robots=[robot0_cfg], objects=[table_cfg, chair_cfg, box_cfg,pork_cfg])

    # Create the environment
    env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)
    pork=env.scene.object_registry("name","pork_ihekpm_0")
    # Reset the robot
    robot = env.robots[0]
    robot.set_position([0, 0, 0])
    robot.set_position_orientation([0, 0, 0], [0, 0, -0.707, 0.707])
    robot.reset()
    robot.keep_still()

    # Make the robot's camera(s) high-res
    for sensor in robot.sensors.values():
        if isinstance(sensor, VisionSensor):
            sensor.image_height = 720
            sensor.image_width = 720

    # Update the simulator's viewer camera's pose so it points towards the robot
    og.sim.viewer_camera.set_position_orientation(
        position=np.array([-2.39951,  2.26469,  2.66227]),
        orientation=np.array([-0.23898481,  0.48475231,  0.75464013, -0.37204802]),
    )

    # Create teleop controller
    action_generator = KeyboardRobotController(robot=robot)

    # Print out relevant keyboard info if using keyboard teleop
    action_generator.print_keyboard_teleop_info()

    # Other helpful user info
    print("Running demo with grasping mode {}.".format(grasping_mode))
    print("Press ESC to quit")
    
    from collections import OrderedDict

    # Loop control until user quits
    max_steps = -1 if not short_exec else 100
    step = 0 
    pos=np.array([0.5,-1.3,2.1])
    dumbact=OrderedDict([('robot0', np.zeros(11))])
    while step != max_steps:
        # sequentially check the function
        # TODO: how to use the existing object in the scene
        for _ in range(100):
            obs, rew, done, info = env.step(dumbact)
            step += 1
        print("start grasp")        
        action = EasyGrasp(robot, pork, 100)
        for _ in range(100):
            obs, rew, done, info = env.step(dumbact)
            step += 1
        print("start Teleport")
        action = Teleport(robot, pork,[5,0,0])
        for _ in range(100):
            obs, rew, done, info = env.step(dumbact)
            step += 1
        print("start EasyDrop")
        action = EasyDrop(pork, pos, 100)
        for _ in range(100):
            obs, rew, done, info = env.step(dumbact)
            step += 1
        
        action = Capture(robot)
        for _ in range(100):
            obs, rew, done, info = env.step(dumbact)
            step += 1
        
        for i in range(4):
            print(f"start capture pic:{i+1}")
            for _ in range(100):
                obs, rew, done, info = env.step(dumbact)            
            Turn_90(robot)
            Capture(robot, i)

    # Always shut down the environment cleanly at the end
    env.close()


if __name__ == "__main__":
    main()            