import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    toast_191 = registry(env, "french_toast_188")
    breakfast_table_dnsjnv_0 = registry(env, "breakfast_table_dnsjnv_0")
    toggle_on(robot, toast_191, breakfast_table_dnsjnv_0)
    donothing(env)
