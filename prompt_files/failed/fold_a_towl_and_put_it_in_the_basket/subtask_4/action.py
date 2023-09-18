import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the bath_towel_85 from the wicker_basket_84.
    bath_towel_85 = registry(env,"bath_towel_85")
    EasyGrasp(robot, bath_towel_85)
    donothing(env)
