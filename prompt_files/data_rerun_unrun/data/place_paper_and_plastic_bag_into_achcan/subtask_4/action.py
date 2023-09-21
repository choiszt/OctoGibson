import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the wrapping paper into the trash can
    wrapping_paper_276 = registry(env,"wrapping_paper_276")
    trash_can_279 = registry(env,"trash_can_279")
    put_inside(robot, wrapping_paper_276, trash_can_279)
    donothing(env)
