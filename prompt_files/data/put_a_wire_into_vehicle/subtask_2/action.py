import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Pick up the copper wire
    copper_wire_282 = registry(env,"copper_wire_282")
    EasyGrasp(robot, copper_wire_282)
    donothing(env)
