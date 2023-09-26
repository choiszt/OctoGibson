import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    baking_box_87 = registry(env, "pizza_box_86")
    EasyGrasp(robot, baking_box_87)
    donothing(env)
