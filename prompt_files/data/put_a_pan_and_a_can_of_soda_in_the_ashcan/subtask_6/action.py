import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the can of soda into the trash can
    can_of_soda_89 = registry(env,"can_of_soda_89")
    trash_can_85 = registry(env,"trash_can_85")
    put_inside(robot, can_of_soda_89, trash_can_85)
    donothing(env)
