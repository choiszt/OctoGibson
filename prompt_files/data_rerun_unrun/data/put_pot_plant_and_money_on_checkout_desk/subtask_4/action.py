import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the pot plant on the checkout desk
    pot_plant_152 = registry(env,"pot_plant_152")
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    put_ontop(robot, pot_plant_152, checkout_counter_sckdal_0)
    donothing(env)
