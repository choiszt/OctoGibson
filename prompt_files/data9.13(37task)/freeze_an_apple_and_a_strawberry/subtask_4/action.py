import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the strawberry from the tray
    strawberry = registry(env, "strawberry_91")
    EasyGrasp(robot, strawberry)
    donothing(env)
