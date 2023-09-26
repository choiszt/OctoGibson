import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    heat(env, 'leaflet-279')
    EasyGrasp(robot, camera)
    donothing(env)
