import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    clothes_dryer_zlmnfg_0 = registry(env, "flower_mylblj_0")
    MoveBot(env, robot, clothes_dryer_zlmnfg_0, camera)
    donothing(env)
