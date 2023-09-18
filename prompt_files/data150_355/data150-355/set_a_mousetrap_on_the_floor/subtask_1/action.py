import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bed
    bed_zrumze_0 = registry(env,"bed_zrumze_0")
    MoveBot(env, robot, bed_zrumze_0, camera)
    donothing(env)
