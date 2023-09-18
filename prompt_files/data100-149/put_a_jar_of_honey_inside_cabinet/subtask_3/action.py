import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the front of the jar of honey
    jar_of_honey_85 = registry(env,"jar_of_honey_85")
    MoveBot(env, robot, jar_of_honey_85, camera)
    donothing(env)
