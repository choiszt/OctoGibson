import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    suitcase_276 = registry(env, "electric_switch_wseglt_0")
    MoveBot(env, robot, suitcase_276, camera)
    donothing(env)
