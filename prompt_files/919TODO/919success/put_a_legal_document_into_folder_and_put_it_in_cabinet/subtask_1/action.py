import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the legal document
    legal_document_188 = registry(env,"legal_document_188")
    MoveBot(env, robot, legal_document_188, camera)
