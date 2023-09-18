import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Register the object 'hamburger_276'
    hamburger_276 = registry(env,"hamburger_276")
    # Subtask 6: Move the robot to the hamburger_276
    MoveBot(env, robot, hamburger_276, camera)
    donothing(env)
    # Subtask 7: Grasp the hamburger_276
    EasyGrasp(robot, hamburger_276)
    donothing(env)
