import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Take the cooked garlic clove out of the stove
    garlic_clove_209 = registry(env,"garlic_clove_209")
    stove_igwqpj_0 = registry(env,"stove_igwqpj_0")
    EasyGrasp(robot, garlic_clove_209)
    donothing(env)
