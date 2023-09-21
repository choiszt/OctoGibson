import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the hand_towel_82 from the wicker_basket_84.
    hand_towel_82 = registry(env,"hand_towel_82")
    EasyGrasp(robot, hand_towel_82)
    donothing(env)
