import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the plate
    plate_88 = registry(env,"plate_88")
    MoveBot(env, robot, plate_88, camera)
    donothing(env)
    
    # Subtask 2: Grasp the plate
    EasyGrasp(robot, plate_88)
    donothing(env)
    
    # Subtask 3: Move to the breakfast table
    breakfast_table_idnnmz_0 = registry(env,"breakfast_table_idnnmz_0")
    MoveBot(env, robot, breakfast_table_idnnmz_0, camera)
    donothing(env)
    
    # Subtask 4: Put the plate on the breakfast table
    put_ontop(robot, plate_88, breakfast_table_idnnmz_0)
    donothing(env)
