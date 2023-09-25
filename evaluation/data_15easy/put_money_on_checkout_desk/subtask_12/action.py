import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    checkoutdesk = (env, 'checkout-counter-sckdal_0')
    money = (env, 'money_142,money_143')
    toggle_on(robot, camera, robot)
