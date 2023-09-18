import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the teddy bear
    teddy_bear_88 = registry(env,"teddy_bear_88")
    MoveBot(env, robot, teddy_bear_88, camera)
    donothing(env)
