import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    book = registry(env, "notebook_277")
    car = registry('car_275')
