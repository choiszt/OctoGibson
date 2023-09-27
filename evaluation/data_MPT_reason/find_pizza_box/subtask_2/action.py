import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    pizzabox_85 = registry(env, "pizza_box_86")
    EasyGrasp(robot, pizzabox_85)
    donothing(env)
