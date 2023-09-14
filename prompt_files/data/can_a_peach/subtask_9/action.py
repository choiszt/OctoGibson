import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the peach inside the jar
    peach = registry(env, "peach_173")
    jar = registry(env, "jar_171")
    put_inside(robot, peach, jar)
    donothing(env)
