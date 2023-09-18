import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the microwave
    microwave_bfbeeb_0 = registry(env,"microwave_bfbeeb_0")
    MoveBot(env, robot, microwave_bfbeeb_0, camera)
    donothing(env)
