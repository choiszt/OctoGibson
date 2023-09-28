import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fuel_storage_tanks_194 = registry(env, "shelf_njwsoa_0")
    EasyGrasp(robot, fuel_storage_tanks_194)
    donothing(env)
