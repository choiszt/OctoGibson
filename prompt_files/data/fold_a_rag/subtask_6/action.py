import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: If the rag is foldable, fold the rag.
    rag_194 = registry(env,"rag_194")
    for obj in [(bath_towel_191, (['heatable', 0], ['freezable', 0], ['unfoldable', 1], ['foldable', 0]), 1.47),(hand_towel_189, (['heatable', 0], ['freezable', 0], ['unfoldable', 1], ['foldable', 0]), 1.66),(washer_omeuop_0, (['togglable', 0], ['openable', 0], ['heatable', 0], ['freezable', 0]), 1.7),(hand_towel_190, (['heatable', 0], ['freezable', 0], ['unfoldable', 0], ['foldable', 0]), 1.36),(bath_towel_193, (['heatable', 0], ['freezable', 0], ['unfoldable', 1], ['foldable', 0]), 1.48),(hamper_188, (['heatable', 0], ['freezable', 0]), 1.99),(rag_194, (['heatable', 0], ['freezable', 0], ['unfoldable', 0], ['foldable', 0]), 0.38),(clothes_dryer_zlmnfg_0, (['togglable', 0], ['heatable', 0], ['freezable', 0]), 1.47),(bath_towel_192, (['heatable', 0], ['freezable', 0], ['unfoldable', 1], ['foldable', 0]), 1.53)]:
        if obj[0] == 'rag_194' and ('foldable', 1) in obj[1]:
            fold(robot, rag_194)
            donothing(env)
            break
