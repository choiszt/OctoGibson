def act(robot,env,camera):
    # Subtask 1: Move therobot to theleaf
    leaf_275 = registry(env,"leaf_275")
    MoveBot(env, robot, leaf_275, camera)
    donothing(env)

