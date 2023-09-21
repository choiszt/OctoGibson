import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 3: Move the robot to the credit card terminal (cash register).
    credit_card_terminal_142 = registry(env, "credit_card_terminal_142")
    MoveBot(env, robot, credit_card_terminal_142, camera)
    donothing(env)
