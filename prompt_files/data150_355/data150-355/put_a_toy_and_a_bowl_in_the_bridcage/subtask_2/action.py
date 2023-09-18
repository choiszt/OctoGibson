import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the toy_figure_191
    toy_figure_191 = registry(env,"toy_figure_191")
    EasyGrasp(robot, toy_figure_191)
    donothing(env)
