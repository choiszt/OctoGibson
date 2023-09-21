import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the jar from the bottom cabinet
    jar = registry(env, "jar_171")
    EasyGrasp(robot, jar)
    donothing(env)
