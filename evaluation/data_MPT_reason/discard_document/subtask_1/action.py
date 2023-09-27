import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    desk_erg_0 = registry(env, "clothes_dryer_zlmnfg_0")
    MoveBot(env, robot, desk_erg_0, camera)
    donothing(env)
