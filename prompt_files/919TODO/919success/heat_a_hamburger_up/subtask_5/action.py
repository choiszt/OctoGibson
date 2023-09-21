import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Close the microwave
    microwave = registry(env,"microwave_bfbeeb_0")
    close(robot, microwave)
    donothing(env)
