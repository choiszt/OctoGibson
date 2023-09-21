import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the cooked garlic clove on the countertop
    garlic_clove_209 = registry(env,"garlic_clove_209")
    countertop_tpuwys_6 = registry(env,"countertop_tpuwys_6")
    put_ontop(robot, garlic_clove_209, countertop_tpuwys_6)
    donothing(env)
