import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    cup_85 = registry(env, "cup_of_yogurt_89")
    EasyGrasp(robot, cup_85)
    donothing(env)
