import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Check if the mattress is on the bed. If not, grasp the mattress and put it on the bed.
    mattress = registry(env, "mattress_82")
    bed = registry(env, "bed_zrumze_0")
    if ('mattress_82', 'ontop', 'bed_zrumze_0') not in env.relations:
        EasyGrasp(robot, mattress)
        donothing(env)
        put_ontop(robot, mattress, bed)
        donothing(env)
