import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leaf_276 = registry('leafe_276')
    unfold(robot, env, robot)
