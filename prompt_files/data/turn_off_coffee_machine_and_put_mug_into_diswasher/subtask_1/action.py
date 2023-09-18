import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the coffee machine
    coffee_maker_188 = registry(env,"coffee_maker_188")
    MoveBot(env, robot, coffee_maker_188, camera)
    donothing(env)
