import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Take out the lasagna
    lasagna_85 = registry(env,"lasagna_85")
    EasyGrasp(robot, lasagna_85)
    donothing(env)
