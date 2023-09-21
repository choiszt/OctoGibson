import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the legal document
    legal_document_188 = registry(env,"legal_document_188")
    EasyGrasp(robot, legal_document_188)
    donothing(env)
