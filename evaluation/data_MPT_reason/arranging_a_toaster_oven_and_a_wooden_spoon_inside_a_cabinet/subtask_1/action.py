import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    Cabinet_qohxjq_0 = registry(env, "carpet_ctclvd_0")
    MoveBot(env, robot, Cabinet_qohxjq_0, camera)
    donothing(env)
