import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    carrot = registry(env, "carrot_151")
    MoveBot(env, robot, carrot, camera)
    donothing(env)
