import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the jar of honey
    jar_of_honey_85 = registry(env,"jar_of_honey_85")
    EasyGrasp(robot, jar_of_honey_85)
    donothing(env)
