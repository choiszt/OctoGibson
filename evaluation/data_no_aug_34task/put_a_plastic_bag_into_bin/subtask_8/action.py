import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    plastic_trash_can = registry(plastic_trash_can, 'plastic-trash-can-275')
    MoveBot(env, robot, plastic_trash_can, camera)
