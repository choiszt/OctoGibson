import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    plastic_baasket_277 = registry(plastic_baasket_277, 'plastic_basquet_277')
    MoveBot(env, robot, plastic_baasket_277, camera)
    donothing(env)
