import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    #Subtask 1: Move the robot close to the brisket
    brisket = registry(env, "brisket_189")
    MoveBot(env, robot, brisket, camera)
    donothing(env)
