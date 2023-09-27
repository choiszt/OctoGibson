import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    chocolates = registry(env, "box_of_chocolates_143")
    EasyGrasp(robot, chocolates)
    donothing(env)
