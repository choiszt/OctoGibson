import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, robot):
    recyclingsbag = registry(env, "recycling_bin_188")
    EasyGrasp(robot, recyclingsbag)
    donothing(env)
