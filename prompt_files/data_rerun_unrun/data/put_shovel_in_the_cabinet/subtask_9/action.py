import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the cabinet
    bottom_cabinet_jrhgeu_0 = registry(env,"bottom_cabinet_jrhgeu_0")
    MoveBot(env, robot, bottom_cabinet_jrhgeu_0, camera)
    donothing(env)
