import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    box_fcfschoc_197 = registry(env, "box_of_chocolates_143")
    MoveBot(env, robot, box_fcfschoc_197, camera)
    donothing(env)
