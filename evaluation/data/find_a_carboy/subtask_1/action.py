import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    reagent = registry(env, "reagent_bottle_189")
    MoveBot(env, robot, reagent, camera)
