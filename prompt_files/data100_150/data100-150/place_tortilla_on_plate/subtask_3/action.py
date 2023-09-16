import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 3: Move to the stove
    stove_rgpphy_0 = registry(env, "stove_rgpphy_0")
    MoveBot(env, robot, stove_rgpphy_0, camera)
    donothing(env)
