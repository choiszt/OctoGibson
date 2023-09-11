import omnigibson as og
from omnigibson import object_states
reverse=lambda states:{value:key for key,value in states.items()}
unary_states={object_states.Cooked:"cookable",object_states.Burnt:"burnable",object_states.Frozen:"freezable",object_states.Heated:"heatable",
object_states.Open:"openable",object_states.ToggledOn:"togglable",object_states.Folded:"foldable",object_states.Unfolded:"unfoldable"}
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
reversed_unary_states,reversed_binary_states=reverse(unary_states),reverse(binary__states)

def verify_taskgoal(env,bddl_name,states,targets):
    bddl_map=env.task.load_task_metadata()['inst_to_name']
    og_obj=bddl_map[bddl_name] #stove_rgpphy_0
    states_status=reversed_unary_states[states] # CLASS object_states
    registered_obj=env.scene.object_registry("name", og_obj)
    return registered_obj.states[states_status]._get_value()==int(targets)


def verify_binary_taskgoal(env,bddl_name1,states,bddl_name2,targets):
    bddl_map=env.task.load_task_metadata()['inst_to_name']
    og_obj1=bddl_map[bddl_name1] #stove_rgpphy_0
    og_obj2=bddl_map[bddl_name2] #stove_rgpphy_1
    obj1 = env.scene.object_registry("name", og_obj1)
    obj2 = env.scene.object_registry("name", og_obj2)
    if states == 'inside':
        """
        obj1 inside obj2
        """
        pos1 = obj1.get_position()
        pos2 = obj2.get_position()
        bbox1 = obj1.native_bbox
        bbox2 = obj2.native_bbox
        if pos1[0] + 0.5 * bbox1[0] <= pos2[0] + 0.5 * bbox2[0] and pos1[0] - 0.5 * bbox1[0] >= pos2[0] - 0.5 * bbox2[0] and \
                pos1[1] + 0.5 * bbox1[1] <= pos2[1] + 0.5 * bbox2[1] and pos1[1] - 0.5 * bbox1[1] >= pos2[1] - 0.5 * bbox2[1] and \
                pos1[2] + 0.5 * bbox1[2] <= pos2[2] + 0.5 * bbox2[2] and pos1[2] - 0.5 * bbox1[2] >= pos2[2] - 0.5 * bbox2[2]:
            v = 1
        else:
            v = 0
        return v == int(targets)
    elif states == 'ontop':
        """
        obj1 ontop obj2
        """
        pos1 = obj1.get_position()
        pos2 = obj2.get_position()
        # bbox1 = obj1.native_bbox
        # bbox2 = obj2.native_bbox
        if pos1[2] >= pos2[2]:
            v = 1
        else:
            v = 0
        return v == int(targets)
    else:
        return True
        # raise Exception(f"Not supported states {states}")