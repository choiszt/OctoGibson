import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    (stove_188, staw191) = registry(env, "toilet_paper_278")
    EasyGrasp(camera, robot)
    donothing()
