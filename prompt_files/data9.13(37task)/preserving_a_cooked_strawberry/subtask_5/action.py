import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the cooked strawberry in the jar
    strawberry_201 = registry(env,"strawberry_201")
    jar_212 = registry(env,"jar_212")
    put_inside(robot, strawberry_201, jar_212)
    donothing(env)
