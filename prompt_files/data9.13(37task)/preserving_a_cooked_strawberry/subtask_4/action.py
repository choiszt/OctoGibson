import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the jar
    jar_212 = registry(env,"jar_212")
    MoveBot(env, robot, jar_212, camera)
    donothing(env)
