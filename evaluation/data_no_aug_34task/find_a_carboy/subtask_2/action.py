import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    reagentpot = registry(env, "reagent_bottle_189")
    EasyGrasp(robot, reagentpot)
    donothing(env)
