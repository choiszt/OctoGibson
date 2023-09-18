import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bag of cream cheese from the shopping cart
    bag_of_cream_cheese_144 = registry(env,"bag_of_cream_cheese_144")
    EasyGrasp(robot, bag_of_cream_cheese_144)
    donothing(env)
