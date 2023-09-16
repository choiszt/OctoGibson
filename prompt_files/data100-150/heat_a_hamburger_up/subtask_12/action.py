import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 12: Grasp the heated hamburger from the microwave.
    hamburger_85 = registry(env,"hamburger_85")
    EasyGrasp(robot, hamburger_85)
    donothing(env)
