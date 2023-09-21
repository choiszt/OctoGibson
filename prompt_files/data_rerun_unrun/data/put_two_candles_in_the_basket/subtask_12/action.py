import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the first candle (beeswax_candle_92) in the basket (wicker_basket_88)
    beeswax_candle_92 = registry(env,"beeswax_candle_92")
    wicker_basket_88 = registry(env,"wicker_basket_88")
    put_inside(robot, beeswax_candle_92, wicker_basket_88)
    donothing(env)
