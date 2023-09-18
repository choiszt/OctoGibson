import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Check if the sack is inside the backpack.
    backpack_192 = registry(env,"backpack_192")
    paper_bag_193 = registry(env,"paper_bag_193")
    if ('paper_bag_193', 'inside', 'backpack_192') in env.relations:
        return
    else:
        # Subtask 6: If the sack is not inside the backpack, move the robot to the fridge and open the fridge to check if the sack is inside.
        fridge_dszchb_0 = registry(env,"fridge_dszchb_0")
        MoveBot(env, robot, fridge_dszchb_0, camera)
        donothing(env)
        open(robot, fridge_dszchb_0)
        donothing(env)
