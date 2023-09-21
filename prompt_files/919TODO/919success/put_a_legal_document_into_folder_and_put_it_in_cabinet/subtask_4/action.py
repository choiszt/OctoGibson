import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the legal document into the folder
    legal_document_188 = registry(env,"legal_document_188")
    folder_190 = registry(env,"folder_190")
    put_inside(robot, legal_document_188, folder_190)
    donothing(env)
