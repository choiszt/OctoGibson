import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the box of cereal.
    box_of_cereal_90 = registry(env,"box_of_cereal_90")
    MoveBot(env, robot, box_of_cereal_90, camera)
    donothing(env)
