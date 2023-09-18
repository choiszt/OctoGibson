import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the second candle (beeswax_candle_93)
    beeswax_candle_93 = registry(env,"beeswax_candle_93")
    MoveBot(env, robot, beeswax_candle_93, camera)
    donothing(env)
