import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the insectifuge atomizer
    insectifuge_atomizer_88 = registry(env,"insectifuge_atomizer_88")
    MoveBot(env, robot, insectifuge_atomizer_88, camera)
    donothing(env)
