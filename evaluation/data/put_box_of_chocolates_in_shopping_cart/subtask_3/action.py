import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    baseofcocoa_189 = registry(env, "bag_of_cocoa_144")
    EasyGrasp(robot, baseofcocoa_189)
    donothing(env)
