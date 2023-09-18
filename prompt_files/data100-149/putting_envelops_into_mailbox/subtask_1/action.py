import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to envelope_277
    envelope_277 = registry(env, "envelope_277")
    MoveBot(env, robot, envelope_277, camera)
    donothing(env)
