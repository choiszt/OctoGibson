import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the bowl_189 inside the birdcage_188
    bowl_189 = registry(env,"bowl_189")
    birdcage_188 = registry(env,"birdcage_188")
    put_inside(robot, bowl_189, birdcage_188)
    donothing(env)
