import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    (straw_277, straw_278) = registry(env, "plastic_bag_275")
    MoveBot(env, robot, camera, camera)
    donothing(env)
