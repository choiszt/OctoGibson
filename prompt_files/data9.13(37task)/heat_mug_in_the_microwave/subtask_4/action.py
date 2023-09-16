import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move to the microwave
    microwave = registry(env, "microwave_bfbeeb_0")
    MoveBot(env, robot, microwave, camera)
    donothing(env)
