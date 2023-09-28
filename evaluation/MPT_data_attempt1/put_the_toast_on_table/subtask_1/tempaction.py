def act(robot,env,camera):
    # Subtask 1: Open thebottom cupboard
    bottom_cabinet = registry(env, "bottom_cupboard_no_top_vzzafs_0")
    open(roBot, bottom_cabinet)
    donothing(env)

