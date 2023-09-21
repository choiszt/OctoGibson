import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the first candle (beeswax_candle_92)
    beeswax_candle_92 = registry(env,"beeswax_candle_92")
    EasyGrasp(robot, beeswax_candle_92)
    donothing(env)
