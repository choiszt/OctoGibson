import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Fold the hand_towel_82.
    hand_towel_82 = registry(env,"hand_towel_82")
    fold(robot, hand_towel_82)
    donothing(env)
