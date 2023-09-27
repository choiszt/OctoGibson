import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    tank_207 = registry(env, "tank_88")
    EasyGrasp(robot, tank_207)
    donothing(env)
