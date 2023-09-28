import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    paper_bag_278 = registry(env, "piano_bnxcvw_0")
    MoveBot(env, robot, paper_bag_278, camera)
    donothing(env)
