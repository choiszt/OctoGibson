import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 4: Put the money on the credit card terminal.
    money_146 = registry(env, "money_146")
    credit_card_terminal_142 = registry(env, "credit_card_terminal_142")
    put_ontop(robot, money_146, credit_card_terminal_142)
    donothing(env)
