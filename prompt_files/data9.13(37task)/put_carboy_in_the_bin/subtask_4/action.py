import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the reagent bottle in the bin
    reagent_bottle = registry(env, "reagent_bottle_189")
    bin = registry(env, "recycling_bin_188")
    put_inside(robot, reagent_bottle, bin)
    donothing(env)
