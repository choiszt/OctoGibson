import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the first candle (beeswax_candle_92)
    beeswax_candle_92 = registry(env,"beeswax_candle_92")
    coffee_table_qlmqyy_0 = registry(env,"coffee_table_qlmqyy_0")
    MoveBot(env, robot, coffee_table_qlmqyy_0, camera)
    donothing(env)
