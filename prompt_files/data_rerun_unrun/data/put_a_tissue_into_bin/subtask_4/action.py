import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the tissue into the bin
    toilet_paper_278 = registry(env,"toilet_paper_278")
    recycling_bin_281 = registry(env,"recycling_bin_281")
    put_inside(robot, toilet_paper_278, recycling_bin_281)
    donothing(env)
