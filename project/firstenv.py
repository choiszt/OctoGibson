import omnigibson as og
from omnigibson.macros import gm
from omnigibson import object_states
cfg = dict()
# Define scene
cfg["scene"] = {
    "type": "Scene",
    "floor_plane_visible": True,
}

# Define objects
cfg["objects"] = [
    {
        "type": "DatasetObject", #A USDObject is our most generic object class, and generates an object sourced from the usd_path argument.
        "name": "stove_igwqpj_0",
        "category": "stove",
        "model":"igwqpj",
        # "visual_only": True,
        "scale": [1.0, 1.0, 2.0],
        "position": [0, 0, 0.0],
        "orientation": [0, 0, 0, 1.0],
    },
    {
        "type": "DatasetObject", #A USDObject is our most generic object class, and generates an object sourced from the usd_path argument.
        "name": "pork_ihekpm_0",
        "category": "pork",
        "model":"ihekpm",
        "scale": 0.15,
        "position": [0.50, -0.2, 1.0],
        "orientation": [0, 0, 0, 1.0],
    },    
    
    {
        "type": "DatasetObject",
        "name": "frying_pan_sfbdjn_0",
        "category": "frying_pan",
        "model": "sfbdjn",
        "scale": 1,
        "position": [0.5, -0.1, 1.5],
    },
    
    # {
    #     "type": "PrimitiveObject",
    #     "name": "incredible_box",
    #     "primitive_type": "Cube",
    #     "rgba": [0, 1.0, 1.0, 1.0],
    #     "scale": [0.5, 0.5, 0.1],
    #     "fixed_base": True,
    #     "position": [-1.0, 0, 1.0],
    #     "orientation": [0, 0, 0.707, 0.707],
    # },
    # {
    #     "type": "LightObject",
    #     "name": "brilliant_light",
    #     "light_type": "Sphere",
    #     "intensity": 50000,
    #     "radius": 0.1,
    #     "position": [3.0, 3.0, 4.0],
    # },
]

# Define robots
# cfg["robots"] = [
#     {
#         "type": "Fetch",
#         "name": "skynet_robot",
#         "obs_modalities": ["scan", "rgb", "depth"],
#     },
# ]

# Define task
cfg["task"] = {
    "type": "DummyTask",
    "termination_config": dict(),
    "reward_config": dict(),
}
import numpy as np
# Create the environment
env = og.Environment(cfg)
stove = env.scene.object_registry("name", "stove_igwqpj_0")
pork=env.scene.object_registry("name","pork_ihekpm_0")
# pork.metadata
og.sim.viewer_camera.set_position_orientation(
        position=np.array([-0.32846135, -2.12872749,  5.00727341]),
        orientation=np.array([0.31791102, 0.00140403, 0.00418705, 0.94811027]),
    )
# Allow camera teleoperation
og.sim.enable_viewer_camera_teleoperation()


# Step!
for _ in range(10000):
    # for _ in range(100):
    #     obs, rew, done, info = env.step(env.action_space.sample())
    # a=input("press 1 to open &2 to close")
    # print(pork.states[object_states.OnTop].get_value(stove))
    # if a=="1":
    #     stove.states[object_states.ToggledOn].set_value(True)
    # else:
    #     stove.states[object_states.ToggledOn].set_value(False)
    stove.states[object_states.ToggledOn].set_value(True)
    for _ in range(100):
        obs, rew, done, info = env.step(env.action_space.sample())
        print(pork.states[object_states.Cooked].get_value())
    obs, rew, done, info = env.step(env.action_space.sample())
