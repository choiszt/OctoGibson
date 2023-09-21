import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out the potato
    potato = registry(env,"potato_89")
    EasyGrasp(robot, potato)
    donothing(env)
