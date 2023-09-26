import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    plastic_bowl_275 = registry(env, "plastic_bag_275")
    EasyGrasp(robot, plastic_bowl_275, plastic_bowl_275)
    donothing(env)
