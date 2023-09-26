def act(robot,env,camera):
    # Subtask 1: Move to bottom cabiner
    bottom_cabinet = registry(env, "bottom_hock_ca_1")
    MoveBot(env.table, robot, bottom_cabbage, camera)
    donothing(env)

