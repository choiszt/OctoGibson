def act(robot,env,camera):
    # Subtask 1: Move to the bottom cabinet
    bottom_cabinet_no_top_vzzafs_0 = registry(env,"bottom_cabinet_no_top_vzzafs_0")
    MoveBot(env, robot, bottom_cabinet_no_top_vzzafs_0, camera)
    donothing(env)

