import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, cabinethandle_84):
    cabinethandle_84 = registry(env, "reagent_bottle_189")
    EasyGrasp(env, cabinethandle_84)
    donothing(env)
