import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the fries and burger
    french_fries = registry(env, "french_fries_88")
    hamburger = registry(env, "hamburger_85")
    microwave = registry(env, "microwave_bfbeeb_0")
    
    open(robot, microwave)
    donothing(env)
    
    put_inside(robot, french_fries, microwave)
    donothing(env)
    
    put_inside(robot, hamburger, microwave)
    donothing(env)
    
    toggle_on(robot, microwave)
    donothing(env)
