import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(camera, robot):
    legal_document = registry(env, "legal_document_189")
    MoveBot(env, robot, 'legaldocument_191')
