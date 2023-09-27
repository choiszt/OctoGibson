import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    breakfast_table_dnsjnv_0 = registry(env, "breakfast_table_dnsjnv_0")
    MoveBot(env, robot, breakfast_table_dnsjnv_0, camera)
    donothing(env)
