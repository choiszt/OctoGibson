import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    beet = registry(env, "beet_277")
    wicker_basket = registry(env, "wicker_basket_278")
    unfold(robot, beet, wicker_basket)
    donothing(env)
