import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.asset_utils import get_available_g_scenes, get_available_og_scenes
from omnigibson.utils.ui_utils import choose_from_options, KeyboardRobotController
from omnigibson.sensors import VisionSensor
from collections import OrderedDict
from omnigibson import object_states
import numpy as np
import json
import robot_action as ra

# Configure macros for maximum performance
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_FLATCACHE = True
gm.ENABLE_OBJECT_STATES = True
gm.ENABLE_TRANSITION_RULES = False
import time
from robot_action import *
from scipy.spatial.transform import Rotation as R


def adjust_position(obj, offset):
    pos = obj.get_position()
    pos_x = pos[0] + offset[0]
    pos_y = pos[1] + offset[1]
    pos_z = pos[2] + offset[2]
    adjust_pos = [pos_x, pos_y, pos_z]
    return adjust_pos


def main(random_selection=False, headless=False, short_exec=False):
    scene_cfg = dict(type="InteractiveTraversableScene", scene_model="choiszt")
    robot0_cfg = dict(
        type="Fetch",
        obs_modalities=[
            "rgb",
            "depth",
            "normal",
            "seg_instance",
        ],  # we're just doing a grasping demo so we don't need all observation modalities
        action_type="continuous",
        action_normalize=True,
        visible=False,
    )
    pork_cfg = dict(
        type="DatasetObject",
        name="pork_ihekpm_0",
        category="pork",
        model="ihekpm",
        scale=0.15,
        position=[-0.36788, 3.97716, 0.62028],  # fridge position
        # position= [-0.16995458765489063, 4.899943354378097, 0.93655479931362917],
        orientation=[0, 0, 0, 1.0],
    )
    pan_cfg = dict(
        type="DatasetObject",
        name="frying_pan_sfbdjn_0",
        category="frying_pan",
        model="sfbdjn",
        scale=1,
        position=[-0.07668, 5.73204, 0.93655479931362917],  # fridge position
        orientation=[0, 0, 0, 0],
    )
    cfg = dict(scene=scene_cfg, robots=[robot0_cfg], objects=[pork_cfg, pan_cfg])
    env = og.Environment(
        configs=cfg, action_timestep=1 / 60.0, physics_timestep=1 / 60.0
    )
    pork = env.scene.object_registry("name", "pork_ihekpm_0")
    sink = env.scene.object_registry("name", "sink_czyfhq_0")
    stove = env.scene.object_registry("name", "stove_igwqpj_0")
    fridge = env.scene.object_registry("name", "fridge_xyejdx_0")
    pan = env.scene.object_registry("name", "frying_pan_sfbdjn_0")
    table = env.scene.object_registry("name", "shelf_owvfik_0")
    scenepath = env.scene.get_scene_loading_info("choiszt")
    with open(scenepath, "r") as f:
        scene_info = json.load(f)
    objectinfo = scene_info["state"]["object_registry"]
    robot = env.robots[0]
    robot.set_position([-1.53887291, 4.79978561, 0.01504258])

    action_generator = KeyboardRobotController(robot=robot)
    for sensor in robot.sensors.values():
        if isinstance(sensor, VisionSensor):
            sensor.image_height = 720
            sensor.image_width = 720
    # Print out relevant keyboard info if using keyboard teleop
    action_generator.print_keyboard_teleop_info()
    # og.sim.viewer_camera.set_position_orientation(
    #     position=np.array([-2.48302418,  1.55655398,  2.22882511]),
    #     orientation=np.array([ 0.56621324, -0.0712958 , -0.10258276,  0.81473692]),
    # )
    camera = og.sim.viewer_camera
    bbox_modalities = ["bbox_3d", "bbox_2d_loose"]  # "bbox_2d_tight" not use
    for bbox_modality in bbox_modalities:
        camera.add_modality(bbox_modality)
    camera.focal_length = 10.0
    cam = Camera(camera=camera, env=env, filename="trash")  # initiated camera

    getpos = lambda objectinfo, name: objectinfo[name]["root_link"]["pos"]
    # pan pos
    stove_pan = adjust_position(stove, [-0.16, -0.17, 0.5])
    # pork pos
    tablepos = adjust_position(table, [0, 0, 0.7])
    stovepos = adjust_position(stove, [-0.13, -0.2, 0.76])
    # [-0.36728,5.76531,1.29481]
    # robot pos

    tablepos_bot = adjust_position(robot, [0, 0, 0])
    fridgepos = adjust_position(robot, [0, -0.5, 0])
    stove_bot = adjust_position(robot, [0, 0.9, 0])

    max_steps = -1 if not short_exec else 100
    step = 0
    iter = 0
    while step != max_steps:
        action = np.zeros(11)
        ppposition = robot.get_position()
        cam_position = ra.get_camera_position(ppposition)
        robot_sensor = robot._sensors["robot0:eyes_Camera_sensor"]
        rs_p, rs_o = robot_sensor.get_position_orientation()
        cam.setposition(cam_position, rs_o)
        # quat = rotate_camera_euler()
        # cam.setposition(cam_position, quat)

        # sequentially check the function
        # TODO: how to use the existing object in the scene

        # cam.turn_90()
        donothing(env, action)
        print("detect surroundings!!")
        for i in range(4):
            cam.FlyingCapture(f"{iter}_detect_surroundings")
            iter += 1

            Turn_90(robot)
            rs_o = ra.trans_camera(rs_o)
            cam.setposition(cam_position, rs_o)

            donothing(env, action)

        cam.collectdata_v2(robot)
        donothing(env, action)

        print("move to fridge")
        cam.Update_camera_pos(robot)
        MoveBot(robot, fridgepos)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_move_to_fridge")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("open the fridge")
        fridge.states[object_states.Open].set_value(True)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_open_the_fridge")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("start grasp")
        EasyGrasp(robot, pork, 100)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_start_grasp")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("close the fridge")
        fridge.states[object_states.Open].set_value(False)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_close_the_fridge")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("move to the table")
        cam.Update_camera_pos(robot)
        MoveBot(robot, tablepos_bot)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_move_to_the_table")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("put the pork on the table")
        pork.set_position(tablepos)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_put_the_pork_on_the_table")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("move to the stove")
        cam.Update_camera_pos(robot)
        MoveBot(robot, stove_bot)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_move_to_the_stove")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("open the stove")
        stove.states[object_states.ToggledOn].set_value(True)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_open_the_stove")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("put the pan on the stove")
        # pan.set_position(stove_pan)
        Turn_90(pan, stove_pan)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_put_the_pan_on_the_stove")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("close the stove")
        stove.states[object_states.ToggledOn].set_value(False)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_close_the_stove")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("set the fire of stove")
        stove.states[object_states.ToggledOn].set_value(True)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_set_the_fire_of_stove")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("move to the table")
        cam.Update_camera_pos(robot)
        MoveBot(robot, tablepos_bot)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_move_to_the_table")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("pick the pork")
        EasyGrasp(robot, pork, 100)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_pick_the_pork")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("move to the stove")
        cam.Update_camera_pos(robot)
        MoveBot(robot, stove_bot)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_move_to_the_stove")
        iter += 1
        cam.collectdata_v2(robot)

        donothing(env, action)
        print("put pork on the pan")
        pork.set_position(stovepos)
        donothing(env, action)
        cam.FlyingCapture(f"{iter}_put_pork_on_the_pan")
        iter += 1
        cam.collectdata_v2(robot)

        cam.writejson()

    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()