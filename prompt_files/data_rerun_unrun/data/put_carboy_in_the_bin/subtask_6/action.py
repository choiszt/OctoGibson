import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the reagent bottle (carboy) in the recycling bin (bin)
    recycling_bin = registry(env, "recycling_bin_188")
    reagent_bottle = registry(env, "reagent_bottle_189")
    put_inside(robot, reagent_bottle, recycling_bin)
    donothing(env)
