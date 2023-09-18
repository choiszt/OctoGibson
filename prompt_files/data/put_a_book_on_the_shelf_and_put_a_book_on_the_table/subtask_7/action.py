import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the book on the table
    book = registry(env, "paperback_book_92")
    table = registry(env, "coffee_table_qlmqyy_0")
    put_ontop(robot, book, table)
    donothing(env)
