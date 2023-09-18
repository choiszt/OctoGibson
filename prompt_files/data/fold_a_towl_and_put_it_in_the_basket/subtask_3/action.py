import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the folded hand_towel_82 back into the wicker_basket_84.
    hand_towel_82 = registry(env,"hand_towel_82")
    wicker_basket_84 = registry(env,"wicker_basket_84")
    put_inside(robot, hand_towel_82, wicker_basket_84)
    donothing(env)
