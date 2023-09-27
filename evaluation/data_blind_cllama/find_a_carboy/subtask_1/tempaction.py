def act(robot,env,camera):
    # Subtask 1: Open the bottom cabinet
    bottom_cabinet = registry(env, "bottom_cabinet_no_top_qudfwe_0")
    open(robot, bottom_cabinet)
    donothing(env)

