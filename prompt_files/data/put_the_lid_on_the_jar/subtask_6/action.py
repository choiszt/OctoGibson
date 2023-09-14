import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put down the jar
    jar = registry(env, "jar_153")
    put_ontop(robot, jar, "table_1")
    donothing(env)
