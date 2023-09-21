import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the bowl
    mixing_bowl_173 = registry(env,"mixing_bowl_173")
    MoveBot(env, robot, mixing_bowl_173, camera)
    donothing(env)
