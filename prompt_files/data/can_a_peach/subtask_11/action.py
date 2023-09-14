import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Put the peach inside the jar
    peach = registry(env, "peach_173")
    jar = registry(env, "jar_172")
    put_inside(robot, peach, jar)
    donothing(env)
