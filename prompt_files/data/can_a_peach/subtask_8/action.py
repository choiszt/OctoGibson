import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Close the jar
    jar = registry(env, "jar_171")
    close(robot, jar)
    donothing(env)
