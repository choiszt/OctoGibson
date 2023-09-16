import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the lid on the jar
    lid = registry(env, "lid_150")
    jar = registry(env, "jar_153")
    put_ontop(robot, lid, jar)
    donothing(env)
