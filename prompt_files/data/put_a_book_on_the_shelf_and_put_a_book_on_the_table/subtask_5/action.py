import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the book from the shelf
    book = registry(env, "paperback_book_92")
    EasyGrasp(robot, book)
    donothing(env)
