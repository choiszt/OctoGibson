import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    choc_bean_84 = registry(env, "bag_of_cocoa_144")
    EasyGrasp(robot, choc_bean_84)
    donothing(env)
