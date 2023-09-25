import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    top_cabinets_dmwxyl_2 = registry(env, "top_cabinet_dmwxyl_2")
    MoveBot(env, robot, top_cabinets_dmwxyl_2, camera)
