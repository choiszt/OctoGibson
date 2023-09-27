import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bottom_cabinet_nddvba_0 = registry(env, "bottom_cabinet_qacthv_0")
    MoveBot(env, robot, bottom_cabinet_nddvba_0, camera)
    donothing(env)
