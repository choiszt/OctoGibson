import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(env, camera, robot):
    unfold(env, camera)
    donothing(env)
