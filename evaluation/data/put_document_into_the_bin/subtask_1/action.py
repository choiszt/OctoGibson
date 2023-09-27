import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    document_189 = registry(env, "legal_document_189")
    EasyGrasp(robot, document_189)
    donothing(env)
