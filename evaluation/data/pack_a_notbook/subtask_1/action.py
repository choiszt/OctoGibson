import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    notetpad_189 = registry(env, "pen_83")
    EasyGrasp(robot, notetpad_189)
    donothing(env)
