import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the toy_figure_191 inside the birdcage_188
    toy_figure_191 = registry(env,"toy_figure_191")
    birdcage_188 = registry(env,"birdcage_188")
    put_inside(robot, toy_figure_191, birdcage_188)
    donothing(env)
