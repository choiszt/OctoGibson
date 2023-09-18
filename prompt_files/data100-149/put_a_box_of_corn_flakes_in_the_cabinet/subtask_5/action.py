import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the box of corn flakes in the cabinet.
    box_of_corn_flakes_87 = registry(env,"box_of_corn_flakes_87")
    bottom_cabinet_no_top_vzzafs_0 = registry(env,"bottom_cabinet_no_top_vzzafs_0")
    put_inside(robot, box_of_corn_flakes_87, bottom_cabinet_no_top_vzzafs_0)
    donothing(env)
