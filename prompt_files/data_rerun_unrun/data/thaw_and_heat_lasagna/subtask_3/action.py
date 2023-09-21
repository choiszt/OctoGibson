import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the lasagna
    oven_wuinhm_0 = registry(env,"oven_wuinhm_0")
    MoveBot(env, robot, oven_wuinhm_0, camera)
    donothing(env)
    open(robot, oven_wuinhm_0)
    donothing(env)
    put_inside(robot, lasagna_85, oven_wuinhm_0)
    donothing(env)
    close(robot, oven_wuinhm_0)
    donothing(env)
    toggle_on(robot, oven_wuinhm_0)
    donothing(env)
