import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Take a jar out of the bottom cabinet
    jar = registry(env, "jar_172")
    EasyGrasp(robot, jar)
    donothing(env)
