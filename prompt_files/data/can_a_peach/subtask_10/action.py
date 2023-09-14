import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Open jar_171
    jar = registry(env, "jar_171")
    open(robot, jar)
    donothing(env)
