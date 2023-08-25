

import pkg_resources
import os
import json
from omnigibson import object_states
reverse=lambda states:{value:key for key,value in states.items()}
unary_states={object_states.Cooked:"cooked",object_states.Burnt:"burnt",object_states.Frozen:"frozen",object_states.Heated:"hot",
                         object_states.Open:"open",object_states.ToggledOn:"toggled_on",object_states.Folded:"folded",object_states.Unfolded:"unfolded"}
binary__states={
    object_states.Inside: "inside",
    object_states.NextTo: "nextto",
    object_states.OnTop: "ontop",
    object_states.Under: "under",
    object_states.Touching: "touching",
    object_states.Covered: "covered",
    object_states.Contains: "contains",
    object_states.Saturated: "saturated",
    object_states.Filled: "filled",
    object_states.AttachedTo: "attached",
    object_states.Overlaid: "overlaid",
    object_states.Draped: "draped"
}
reversed_unary_states,reversed_binary__states=reverse(unary_states),reverse(binary__states)


def verify_inv(env, robot, states):
    return env.scene.object_registry("name", states) in robot.inventory # we need to transfer variable to str

def verify_obj_2(obj, states, value):
    states_status=reversed_unary_states[states] # CLASS object_states
    return states_status._get_value(obj)==value
    

def verify_obj_3(obj1, states, obj2, value):
    states_status=reversed_binary__states[states] # CLASS object_states
    return states_status._get_value(obj1,obj2)==value

def save_response(path, response):
    responses = {}
    responses['response'] = response
    with open(os.path.join(path, 'response.json'), 'w') as f:
        f.write(json.dumps(responses, indent=4))
        

def save_feedback(path, subtask, code, error, critic, reset, main_succeed):
    feedback = {}
    feedback['subtask'] = subtask
    feedback['code'] = code
    feedback['error'] = error
    feedback['critic'] = critic
    feedback['reset'] = reset
    feedback['main_succeed'] = main_succeed
    with open(path, 'w') as f:
        f.write(json.dumps(feedback, indent=4))
        
if __name__ == '__main__':
    subtask_iter = 1
    retry = 1
    save_path = f_mkdir(os.path.join('./data', str('cook the bacon')))
    sub_save_path = f_mkdir(os.path.join(save_path, f"subtask_{subtask_iter}"))
    retry_data_path = f_mkdir(os.path.join(sub_save_path, f"retry_{retry}"))
    save_response(retry_data_path, response={}, error='check')
    save_input(retry_data_path, input='this is a test')
    
    