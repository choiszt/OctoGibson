import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    (straw, staw277) = registry(env, "plastic_bag_275")
    MoveBot(env, robot, robot, camera)
    donothing(env)
