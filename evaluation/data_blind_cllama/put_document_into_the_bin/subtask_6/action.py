import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    legal_document_189 = registry(env, "legal_document_189")
    recycling_bin_188 = registry(env, "recycling_bin_188")
    unfold(robot, legal_document_189, recycling_bin_188)
    donothing(env)
