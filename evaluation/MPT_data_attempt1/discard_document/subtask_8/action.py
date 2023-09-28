import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(camera, robot):
    top_cabinet = registry(env, "top_cabinet_dmwxyl_0")
