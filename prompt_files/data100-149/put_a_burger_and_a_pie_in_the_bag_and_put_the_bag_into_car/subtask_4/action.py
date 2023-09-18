import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the bag
    # Since the bag is not observed in the environment, we need to explore the environment to find it.
    # Here we assume that the bag might be inside the suitcase, so we will open the suitcase to find the bag.
    # However, the suitcase is not openable, so we need to revise our plan.
    # Let's try to find the bag inside the suitcase_285, which is closer to the robot.
    suitcase_285 = registry(env,"suitcase_285")
    open(robot, suitcase_285)
    donothing(env)
