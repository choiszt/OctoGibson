import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    straw = registry(env, "plastic_bag_275")
    MoveBot(env, robot, straw, camera)
    donothing(env)
