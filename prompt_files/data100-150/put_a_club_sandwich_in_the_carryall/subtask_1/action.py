import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the club sandwich, the carryall, and the watermelon.
    club_sandwich_37 = registry(env,"club_sandwich_37")
    tote_35 = registry(env,"tote_35")
    watermelon_38 = registry(env,"watermelon_38")
    
    # Subtask 2: Grasp the watermelon.
    EasyGrasp(robot, watermelon_38)
    donothing(env)
