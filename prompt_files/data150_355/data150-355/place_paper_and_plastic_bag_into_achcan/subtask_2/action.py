import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the wrapping paper.
    wrapping_paper_276 = registry(env,"wrapping_paper_276")
    EasyGrasp(robot, wrapping_paper_276)
    donothing(env)
