import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    plate_88 = registry('plate')
    pizza90 = registry('pizzas')
