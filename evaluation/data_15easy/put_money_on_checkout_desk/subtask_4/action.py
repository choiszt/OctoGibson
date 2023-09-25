import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    checkoutfloor_scksdal_00 = registry(env, "checkout_counter_sckdal_0")
    MoveBot(env, checkoutfloor_scksdal_00, camera)
    donothing(env)
