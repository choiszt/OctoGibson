import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the second candle (beeswax_candle_93)
    beeswax_candle_93 = registry(env,"beeswax_candle_93")
    EasyGrasp(robot, beeswax_candle_93)
    donothing(env)
