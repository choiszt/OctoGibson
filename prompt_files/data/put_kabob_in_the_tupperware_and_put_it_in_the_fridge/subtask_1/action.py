import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the kabob
    kabob_85 = registry(env,"kabob_85")
    MoveBot(env, robot, kabob_85, camera)
    donothing(env)
    # Subtask 2: Grasp the kabob
    EasyGrasp(robot, kabob_85)
    donothing(env)
