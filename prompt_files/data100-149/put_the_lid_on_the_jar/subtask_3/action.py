import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out the jar
    jar_153 = registry(env, "jar_153")
    EasyGrasp(robot, jar_153)
    donothing(env)
