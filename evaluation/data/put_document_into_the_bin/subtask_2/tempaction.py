def act(robot,env,camera):
    # Subtask 2: Move to the bin.
    recycling_bin_188 = registry(env,"recycling_bin_188")
    MoveBot(env, robot, recycling_bin_188, camera)
    donothing(env)

