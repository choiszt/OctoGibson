import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    plastic_recycling = registry(plastic_recycling, 'plastic_basket_281')
