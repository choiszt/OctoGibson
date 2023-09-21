import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the book (hardback_91)
    hardback_91 = registry(env,"hardback_91")
    MoveBot(env, robot, hardback_91, camera)
    donothing(env)
