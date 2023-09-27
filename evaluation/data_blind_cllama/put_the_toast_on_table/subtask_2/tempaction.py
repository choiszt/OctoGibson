def act(robot,env,camera):
    # Subtask 2: Open the bottom cabinet
    bottom_cabinet_no_top_vzzafs_0 = registry(env,"bottom_cabinet_no_top_vzzafs_0")
    open(robot, bottom_cabinet_no_top_vzzafs_0)
    donothing(env)

