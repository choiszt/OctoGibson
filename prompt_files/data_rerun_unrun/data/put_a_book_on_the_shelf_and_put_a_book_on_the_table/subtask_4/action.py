import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the book on the shelf
    book = registry(env, "paperback_book_92")
    shelf = registry(env, "shelf_njwsoa_0")
    put_ontop(robot, book, shelf)
    donothing(env)
